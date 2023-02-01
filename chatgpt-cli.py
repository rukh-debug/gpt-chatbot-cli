#!/usr/bin/env python3
import openai
import os
import termcolor
from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.styles import Style

presets = {
    "Chat": {
        "message": "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.",
        "inject": {
            "state": True,
            "start": "AI:",
            "end": "Human:"
        },
    },
    "Q&A": {
        "message": "I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with 'Unknown'.\n",
        "inject": {
            "state": True,
            "start": "A:",
            "end": "Q:"
        },
    },
    "Grammar Correction": {
        "message": "Correct this to standard English:\n",
        "inject": {
            "state": False,
        }
    },
    "Eli5": {
        "message":"Summarize this for a second-grade student:\n",
        "inject": {
            "state": False,
        }
    },
    "Custom": {
        "message": "",
        "inject": {
            "state": False
        }
    }
}
def api_key_helper():
    return [('class:api-key-helper', 'Set the environment variable OPENAI_API_KEY to avoid further prompts. ')]

def chat_prompt_helper(on, message):
        return [('class:chat-prompt-helper', "Mode: "+on+"\n"+message)]

style = Style.from_dict({
    'api-key-helper': '#fc802d bg:#282828 bold',
    'chat-prompt-helper': "#504945 bg:#fbf0c9 bold"
})

def check_api_key_validity(api_key, where):
    if(where == "prompt"):
        print("Found env variable OPENAI_API_KEY")
    print("Checking for validity")
    try:
        openai.api_key = api_key
        openai.Model.list()
        print(termcolor.colored(f"API key is valid", 'light_green', attrs=["bold"]))
    except openai.OpenAIError as e:
        print(termcolor.colored(f"Invalid API key", 'light_red', attrs=["bold"]) + "\nGrab your API key from: "+termcolor.colored(f"https://beta.openai.com/account/api-keys", 'light_blue', attrs=["underline"]))
        exit()
# import api key
api_key = os.environ.get("OPENAI_API_KEY")

if not api_key:
    try:
        api_key = prompt("Please enter your OpenAI API key: ", bottom_toolbar=api_key_helper, style=style)
        check_api_key_validity(api_key, "not-prompt")
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)
else:
    check_api_key_validity(api_key, "prompt")

# set model and temperature
model = "text-davinci-003"
temperature = 0.9

# Initialize conversation_history
conversation_history = ''

try:
    # Ask user to pick a preset
    print("Please choose a preset:")
    
    # Print the options
    options = list(presets.keys())
    print("Please select an option by number:")
    for i, key in enumerate(options):
        print(f"{i+1}: {key}")

    # Validate user input
    class NumberValidator(Validator):
        def validate(self, document):
            try:
                value = int(document.text)
                if value not in range(1, len(options) + 1):
                    raise ValueError()
            except ValueError:
                raise ValidationError(
                    message='Please enter a number between 1 and {}'.format(len(options)),
                    cursor_position=len(document.text))

    # Ask the user to pick an option
    selected_num = prompt('Option: ', validator=NumberValidator())

    # Get the selected option
    selected_num = int(selected_num)
    chosen_preset = list(presets.keys())[selected_num - 1]
    
    # Append preset message to conversation_history
    if chosen_preset in presets:
        conversation_history += presets[chosen_preset]["message"]
    else:
        print("Invalid preset chosen, please try again.")
        exit()
        
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
    while True:
        # get user input
        user_input = prompt(end_string, bottom_toolbar=chat_prompt_helper(chosen_preset, presets[chosen_preset]["message"]), style=style)

        if user_input.lower() in ["exitgpt","exit"]:
            break
        # generate response
        response = openai.Completion.create(
            engine=model,
            prompt=conversation_history + end_string + user_input + "\n" + start_string,
            temperature=temperature,
            max_tokens=1024,
        )
        if (state):
            conversation_history += end_string + user_input + "\n" + response.choices[0].text + "\n"
        else:
            conversation_history = presets[chosen_preset]["message"]
        # print response with termcolor
        print(termcolor.colored(f"{start_string}{response.choices[0].text}", 'light_yellow'))

except KeyboardInterrupt:
    print("Exiting...")
    exit(0)

