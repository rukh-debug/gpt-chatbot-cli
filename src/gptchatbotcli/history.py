from gptchatbotcli.database import get_all_chat_history

def chat_history_picker():
  chat_history = get_all_chat_history()
  if (len(chat_history) == 0):
    print("No chat history found")
    exit()
  else:
    print("Pick a chat history:")
    for i in range(len(chat_history)):
      print(f"{i+1}. {chat_history[i]['title']}")
    chat_history_id = int(input("Enter a number: "))
    return chat_history[chat_history_id-1]

