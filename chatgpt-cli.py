#!/bin/python3
import openai
import os
import termcolor
from prompt_toolkit import prompt

def set_env_vars(file_path):
    with open(file_path) as f:
        for line in f:
            key, value = line.strip().split('=')
            os.environ[key] = value

# call the function to set environment variables
set_env_vars('.env')

# import api key
api_key = os.environ.get("OPENAI_API_KEY")
openai.api_key = api_key

# set model and temperature
model = "text-davinci-003"
temperature = 0.9

# Initialize conversation_history
conversation_history = ''

try:
    # start chat loop
    while True:
        # get user input
        user_input = input("User: ")
        if user_input.lower() in ["exitgpt","exit"]:
            break
        prompt = conversation_history + "User:" + user_input + "\n" + "GPT-3:"
        # generate response
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=1024,
        )
        conversation_history += "User:" + user_input + "\n" + response.choices[0].text + "\n"
        
        # print response with termcolor
        print(termcolor.colored(f">>> {response.choices[0].text}", 'light_yellow'))

except KeyboardInterrupt:
    print("Exiting...")
