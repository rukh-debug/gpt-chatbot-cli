from tinydb import TinyDB, Query
import time

db = TinyDB('db/gpt_chatbot_chat_history.json')

def init_chat_history(message, preset, model):
  # generate random string
  _id = str(time.time()).replace(".", "")
  # print("Saving chat history...")
  db.insert({"_id": _id, "preset": preset, 'messages': message, "model": model})
  return _id

def update_chat_history(id, message):
  db.update({'messages': message}, Query()._id == id)
  return True

def get_all_chat_history():
  return db.all()

def defind_chat_title(id, title):
  db.update({'title': title}, Query()._id == id)
