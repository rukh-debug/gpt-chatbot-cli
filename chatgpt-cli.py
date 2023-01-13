#!/bin/python3
import openai
import os
import termcolor
from prompt_toolkit import prompt

presets = {
    "Q&A": {
        "message": "I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with 'Unknown'.\n",
        "inject": {
            "state": True,
            "start": "A:",
            "end": "Q:"
        },
    },
    "Chat": {
        "message": "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.",
        "inject": {
            "state": True,
            "start": "AI:",
            "end": "Human:"
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
    }
}

# import api key
api_key = os.environ.get("OPENAI_API_KEY")
openai.api_key = api_key

# set model and temperature
model = "text-davinci-003"
temperature = 0.9

# Initialize conversation_history
conversation_history = ''

try:
    # Ask user to pick a preset
    print("Please choose a preset:")
    for preset in presets:
        print(f"- {preset}")
    chosen_preset = input("Preset: ")
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
        end_string = ">>>"
        start_string = ">>>"
        
    # start chat loop
    while True:
        # get user input
        user_input = input(end_string + " ")
        
        if user_input.lower() in ["exitgpt","exit"]:
            break
        prompt = conversation_history + end_string + user_input + "\n" + start_string
        
        # generate response
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=1024,
        )
        if (state):
            conversation_history += end_string + user_input + "\n" + response.choices[0].text + "\n"
        else:
            conversation_history = presets[chosen_preset]["message"]
        # print response with termcolor
        print(start_string + termcolor.colored(f"{response.choices[0].text}", 'light_yellow'))

except KeyboardInterrupt:
    print("Exiting...")
    exit()

