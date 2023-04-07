#!/usr/bin/env python3
import os
import termcolor
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
import click

from gptchatbotcli.payloads import presets, chat_complitions_models
from gptchatbotcli.database import init_chat_history, update_chat_history, defind_chat_title
from gptchatbotcli.history import chat_history_picker
from gptchatbotcli.services import print_char_by_char, print_whole_but_color
from gptchatbotcli.openapi_controller import check_api_key_validity, chat_api_call, title_gen

@click.command()
@click.option('--api_key', '-k', help='Openai API key. If not provided, will prompt for it or use the environment variable OPENAI_API_KEY.')
@click.option('--model', '-m', default='gpt-3.5-turbo', help='Model to use for text generation | (default: gpt-3.5-turbo)')
@click.option('--temperature', '-t', default=0.9, type=click.FLOAT, help='Temperature for text generation | (default: 0.9)')
@click.option('--preset', '-p', default='chat', help='Preset mode to use for text generation | (default: Chat) \nAvailable presets: Chat, Q&A, Grammar Correction, Eli5, Custom')
@click.option('--history', '-hs', default=False, is_flag=True, help='Show chat history | (default: False)')
@click.help_option('--help', '-h')
def main(api_key, model, temperature, preset, history):
    """
    A CLI for OpenAI's GPT-3 API.
    Chat with a bot, ask questions, correct grammar, summarize text, and more.

    \b
    Examples:
        gpt-chatbot-cli
        gpt-chatbot-cli --api_key=YOUR_API_KEY
        gpt-chatbot-cli --api_key=YOUR_API_KEY --model=text-davinci-003 --temperature=0.7
        gpt-chatbot-cli -m gpt-4 -t 0.8 -p "q&a"
    """

    def api_key_helper():
        return [('class:api-key-helper', 'Set the environment variable OPENAI_API_KEY to avoid further prompts. ')]


    def chat_prompt_helper(on, message):
            return [('class:chat-prompt-helper', "Mode: "+on+"\n"+message)]

    style = Style.from_dict({
        # make a gruvbox theme for this
        'api-key-helper': '#fc802d bg:#282828 bold',
        # a compatable color for the prompt
        'chat-prompt-helper': 'bg:#000000 #ffffff',
    })

    # import api key
    openai_api_key = os.environ.get("OPENAI_API_KEY") or api_key

    if not openai_api_key:
        try:
            openai_api_key = prompt("Please enter your OpenAI API key: ", bottom_toolbar=api_key_helper, style=style)
            check_api_key_validity(openai_api_key, "not-prompt")
        except KeyboardInterrupt:
            print("Exiting...")
            exit(0)
    else:
        check_api_key_validity(openai_api_key, "prompt")

    # set model and temperature
    lang_model = model
    config_temperature = temperature

    # Initialize conversation_history
    conversation_history = ''
    messages = []
    _id = None

    try:
        # saving chat history initialize
        if history:
            # print("Load chat history... and load preset")
            historyx = chat_history_picker()
            chosen_preset = historyx["preset"]
            _id = historyx["_id"]
            messages = historyx["messages"]
            conversation_history = historyx["messages"]
            lang_model = historyx["model"]
        else:
            chosen_preset = preset
            # replace chosen_preset with preset's actual name with the CASE from presets dictionary
            
            # create a list of lowercase keys from presets dictionary
            preset_keys = [key.lower() for key in presets.keys()]
            
            # find the index of the lowercase version of chosen_preset
            index = preset_keys.index(chosen_preset.lower())
            
            # get the actual key name from presets dictionary using the index
            chosen_preset = list(presets.keys())[index]
            
            # Initialize chat history     
            _id = init_chat_history(messages, chosen_preset, lang_model)
            
            # insert preset message to chat history
            messages.append({
                "role": "system", "content": presets[chosen_preset]["message"]
            })
            
            # update chat history with new initialized message
            update_chat_history(_id, messages)
        
            # we will take care of conversation history later    
            conversation_history += presets[chosen_preset]["message"]
        
        # Replace #END# and #START# with preset's end and start's string if available
        if "inject" in presets[chosen_preset] and presets[chosen_preset]["inject"]["state"]:
            state = True
            end_string = presets[chosen_preset]["inject"]["end"]
            start_string = presets[chosen_preset]["inject"]["start"]
        else:
            state = False
            end_string = ">"
            start_string = ">"
            
        # start chat loop
        count = 0
        while True:
            # render history on term before letting user input new crap
            if (count == 0 and history):
                if lang_model in chat_complitions_models:
                    x = 0
                    for message in messages[1:]:
                        if (x%2 == 0):
                            print(end_string, message["content"])
                        else:
                            print_whole_but_color(start_string, message["content"])
                        x += 1
                else:
                    print("---SORRY FOR BAD RENDERING, WILL MAKE IT BETTER ON NEXT PATCH---")
                    print(conversation_history)
                

            user_input = prompt(end_string + " ", bottom_toolbar=chat_prompt_helper(chosen_preset, presets[chosen_preset]["message"]), style=style)
            if (count == 0 and not history):
                title = title_gen(user_input)
                defind_chat_title(_id, title)
                
            if user_input.lower() in [":q","exit", ":wq", "exitgpt", "exit()"]:
                break


            if lang_model in chat_complitions_models:
                messages.append({
                    "role": "user", "content": user_input
                })
                
                response = chat_api_call(lang_model, messages)
                messages.append({
                    "role": response.choices[0].message.role, "content": response.choices[0].message.content
                })
                update_chat_history(_id, messages)
                print_char_by_char(start_string, response.choices[0].message.content)
            else: 
                response = chat_api_call(lang_model, conversation_history + end_string + user_input + "\n" + start_string, config_temperature, 1024)
                if (state):
                    conversation_history += end_string + user_input + "\n" + response.choices[0].text + "\n"
                else:
                    conversation_history = presets[chosen_preset]["message"]
                update_chat_history(_id, conversation_history)
                print_char_by_char(start_string, response.choices[0].text)
            count += 1

    except Exception as e:
        print(termcolor.colored(f"Error: {e}", 'light_red'))
        exit(1)
    except KeyboardInterrupt:
        print(termcolor.colored(f"Keyboard Interrupt, Exiting...", 'light_red'))
        exit(0)


if __name__ == '__main__':
    main()
