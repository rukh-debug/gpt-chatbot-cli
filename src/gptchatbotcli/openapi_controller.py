import openai
import termcolor

from gptchatbotcli.payloads import chat_complitions_models


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

def title_gen(init_text_input):
  messages = [{
     "role": "system", "content": "You are a title generator, You are given a text input from a user, and according to that text input you will figure out the context of the chat and generate a very short title, maximum 4,5 word of length"
  }]
  messages.append({
    "role": "user",
    "content": init_text_input
  })
  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages,
  )
  return response["choices"][0]["message"]["content"]