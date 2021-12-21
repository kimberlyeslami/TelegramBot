import os
import telebot
import pandas as pd

data = pd.read_csv('Addendum.csv')
type_animal = data[(data.Type=="Animal")]
type_vegetable = data[(data.Type=="Vegetable")]
replies = []

API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.send_message(message.chat.id, "Hello! To start use the command /Play")

@bot.message_handler(commands=["Play"])
def play(message):
  bot.send_message(message.chat.id, "Is it an Animal?")

@bot.message_handler(func=lambda message: True)
def object_type(message):
  response = message.text
  replies.append(response)
  print(replies)
  print(data)
  if replies != None:
    if replies[0] == "Yes":
      print("Here is the data sorted by Animal")
      print(type_animal)
      msg = bot.reply_to(message, 'is it Large?')
      bot.register_next_step_handler(msg, animal_size_large)
    elif replies[0] == "No":
      print("Here is the data sorted by Vegetable")
      print(type_vegetable)
      msg = bot.reply_to(message, 'is it Large?')
      bot.register_next_step_handler(msg, vegetable_size_large)
  
def animal_size_large(message):
  response = message.text
  replies.append(response)
  print(replies)
  if replies[1] == "Yes":
      size_large = type_animal[(data.Size=="Large")]
      print(size_large)
      print("Here is the data sorted by animal size large")
      if len(size_large.index) == 1:
        ans = size_large.iloc[0].Item
        print(ans)
        msg = bot.reply_to(message, f"I think its an {ans}. Am I right?")
        bot.register_next_step_handler(msg, stop_bot)
      elif len(size_large.index) > 1:
        msg = bot.reply_to(message, "Is it Green?")
        bot.register_next_step_handler(msg, animal_colour_green)
  elif replies[1] == "No":
      msg = bot.reply_to(message, 'is it Medium?')
      bot.register_next_step_handler(msg, animal_size_medium)

def animal_size_medium(message):
  response = message.text
  replies.append(response)
  print(replies)
  if replies[2] == "Yes":
      size_medium = type_animal[(data.Size=="Medium")]
      print(size_medium)
      print("Here is the data sorted by animal size medium")
      if len(size_medium.index) == 1:
        ans = size_medium.iloc[0].Item
        print(ans)
        msg = bot.reply_to(message, f"I think its an {ans}. Am I right?")
        bot.register_next_step_handler(msg, stop_bot)
      elif len(size_medium.index) > 1:
        msg = bot.reply_to(message, "Is it Green?")
        bot.register_next_step_handler(msg, animal_colour_green)
  elif replies[2] == "No":
    size_small = type_animal[(data.Size=="Small")]
    print("Here is the data sorted by animal size small")
    print(size_small)
    if len(size_small.index) == 1:
      ans = size_small.iloc[0].Item
      print(ans)
      msg = bot.reply_to(message, f"I think its an {ans}. Am I right?")
      bot.register_next_step_handler(msg, stop_bot)
  
    msg = bot.reply_to(message, 'is it Grey?')
    bot.register_next_step_handler(msg, animal_colour_grey)

def animal_colour_grey(message):
  response = message.text
  replies.append(response)
  print(replies)
  if replies[3] == "Yes":
      animal_size_small = type_animal[(data.Size=="Small")]
      animal_colour_grey = animal_size_small[(data.Colour=="Grey")]
      print("Here is the data sorted by animal size small")
      print(animal_colour_grey)
      if len(animal_colour_grey.index) == 1:
        ans = animal_colour_grey.iloc[0].Item
        print(ans)
        msg = bot.reply_to(message, f"I think its an {ans}. Am I right?")
        bot.register_next_step_handler(msg, stop_bot)
  elif replies[3] == "No":
    animal_size_small = type_animal[(data.Size=="Small")]
    animal_colour_other = animal_size_small[(data.Colour!="Grey")]
    print(animal_colour_other)
    ans = animal_colour_other.iloc[0].Item
    print(ans)
    msg = bot.reply_to(message, f"I think its an {ans}. Am I right?")
    bot.register_next_step_handler(msg, stop_bot)

def animal_colour_green(message):
  replies.append(message.text)
  if replies[3] == 'Yes':
    animal_size_medium= type_animal[(data.Size=="Medium")]
    animal_colour_green = animal_size_medium[(data.Colour=="Green")]
    print("sorted by animal, size medium and colour green")
    print(animal_colour_green)
    if len(animal_colour_green.index) == 1:
      ans = animal_colour_green.iloc[0].Item
      print(ans)
      msg = bot.reply_to(message, f"I think its an {ans}. Am I right?")
      bot.register_next_step_handler(msg, stop_bot)
  elif replies[3] == "No":
    animal_size_medium= type_animal[(data.Size=="Medium")]
    animal_colour_other = animal_size_medium[(data.Colour!="Green")]
    print(animal_colour_other)
    ans = animal_colour_other.iloc[0].Item
    print(ans)
    msg = bot.reply_to(message, f"I think its an {ans}. Am I right?")
    bot.register_next_step_handler(msg, stop_bot)

def vegetable_size_large(message):
  response = message.text
  replies.append(response)
  print(replies)
  if replies[1] == "Yes":
      size_large = type_vegetable[(data.Size=="Large")]
      print(size_large)
      print("Here is the data sorted by vegetable size large")
      if len(size_large.index) == 1:
        ans = size_large.iloc[0].Item
        print(ans)
        msg = bot.reply_to(message, f"I think its an {ans}. Am I right?")
        bot.register_next_step_handler(msg, stop_bot)
  elif replies[1] == "No":
      msg = bot.reply_to(message, 'is it Medium?')
      bot.register_next_step_handler(msg, vegetable_size_medium)

def vegetable_size_medium(message):
  response = message.text
  replies.append(response)
  print(replies)
  if replies[2] == "Yes":
      size_medium = type_vegetable[(data.Size=="Medium")]
      print(size_medium)
      print("Here is the data sorted by vegetable size medium")
      if len(size_medium.index) == 1:
        ans = size_medium.iloc[0].Item
        print(ans)
        msg = bot.reply_to(message, f"I think its an {ans}. Am I right?")
        bot.register_next_step_handler(msg, stop_bot)
      elif len(size_medium.index) > 1:
        msg = bot.reply_to(message, "Is it Orange?")
        bot.register_next_step_handler(msg, vegetable_colour_orange)
  elif replies[2] == "No":
    size_small = type_vegetable[(data.Size=="Small")]
    print("Here is the data sorted by vegetable size small")
    print(size_small)
    if len(size_small.index) == 1:
      ans = size_small.iloc[0].Item
      print(ans)
      msg = bot.reply_to(message, f"I think its an {ans}. Am I right?")
      bot.register_next_step_handler(msg, stop_bot)

def vegetable_colour_orange(message):
  replies.append(message.text)
  if replies[3] == 'Yes':
    vegetable_size_medium= type_vegetable[(data.Size=="Medium")]
    vegetable_colour_orange = vegetable_size_medium[(data.Colour=="Orange")]
    print("sorted by vegetable, size medium and colour orange")
    print(vegetable_colour_orange)
    if len(vegetable_colour_orange.index) == 1:
      ans = vegetable_colour_orange.iloc[0].Item
      print(ans)
      msg = bot.reply_to(message, f"I think its an {ans}. Am I right?")
      bot.register_next_step_handler(msg, stop_bot)
  elif replies[3] == "No":
    vegetable_size_medium= type_vegetable[(data.Size=="Medium")]
    vegetable_colour_other = vegetable_size_medium[(data.Colour!="Orange")]
    print( vegetable_colour_other)
    ans =  vegetable_colour_other.iloc[0].Item
    print(ans)
    msg = bot.reply_to(message, f"I think its an {ans}. Am I right?")
    bot.register_next_step_handler(msg, stop_bot)

def stop_bot(message):
  if message.text != None:
    bot.stop_polling()
    replies.clear()
    bot.send_message(message.chat.id, "Thank you for playing!")
    
bot.polling()

    
