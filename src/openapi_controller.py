import openai
import termcolor

from src.payloads import chat_complitions_models


def check_api_key_validity(api_key, where):
  if(where == "prompt"):
      print("Found env variable OPENAI_API_KEY")
  print("Checking for validity")
  try:
      openai.api_key = api_key
      openai.Model.list()
      print(termcolor.colored(f"API key is valid", 'light_green', attrs=["bold"]))
  except openai.OpenAIError as e:
      print(termcolor.colored(f"Invalid API key", 'light_red', attrs=["bold"]) + "\nGrab your API key from: "+termcolor.colored(f"https://platform.openai.com/account/api-keys", 'light_blue', attrs=["underline"]))
      exit()
#  how to make parameter optional, write in below line

def chat_api_call(engine, messages, temperature=None, max_tokens=None):
  if engine in chat_complitions_models:
    response = openai.ChatCompletion.create(
      model=engine,
      messages=messages,
      # temperature=temperature,
      # max_tokens=max_tokens,
    )
    return response
  else:
    response = openai.Completion.create(
      engine=engine,
      prompt=messages,
      temperature=temperature,
      max_tokens=max_tokens,
    )
    return response
