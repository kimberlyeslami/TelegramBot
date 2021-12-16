import os
import telebot
import pandas as pd

data = pd.read_csv('Addendum.csv')
replies = []

API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Hello'])
def hello(message):
  bot.send_message(message.chat.id, "Hello! To start use the command /Play")

@bot.message_handler(commands=["Play"])
def play(message):
  bot.send_message(message.chat.id, "Is it an Animal?")

@bot.message_handler(func=lambda message: True)
def query1(message):
  response = message.text
  replies.append(response)
  print(replies)
  print(data)
  if replies != None:
    if replies[0] == "Yes":
      animal_sort = data[(data.Type=="Animal")]
      print("Here is the data sorted by Animal")
      print(animal_sort)
    elif replies[0] == "No":
      vegetable_sort = data[(data.Type=="Vegetable")]
      print("Here is the data sorted by Vegetable")
      print(vegetable_sort)
  msg = bot.reply_to(message, 'is it Large?')
  bot.register_next_step_handler(msg, query2)
def query2(message):
  # bot.send_message(message.chat.id,"Is it large?")
  response = message.text
  replies.append(response)
  print(replies)
  data1 = data[(data.Type=="Animal")]
  if replies[1] == "Yes":
      size_large = data1[( data.Size=="Large")]
      print(size_large)
      if len(size_large.index) == 1:
        ans = size_large.iloc[0].Item
        print(ans)
        bot.send_message(message.chat.id, f"I think its an {ans}. Am I right?")
  elif replies[1] == "No":
      vegetable_sort = data[(data.Type=="Vegetable")]
      print("Here is the data sorted by Vegetable")
      print(vegetable_sort)
  # if len(size_large.index) == 1:
  #   ans = size_large.iloc[0].Item
  #   print(ans)
  #   bot.send_message(message.chat.id, ans)

   
bot.polling()

#     # if replies[message.chat.id].filter=="Type":
#     #   if response == "Yes":
#     #     colour = data[data['Colour'] == 'Green']
#     #     replies[message.chat.id] = { filter: "Colour", data: colour }
#     #     bot.send_message(message.chat.id, colour)
# #       else:
# #         colour = data[data['Colour'] != 'Green']
# #       #if colour.len() > 1:
# #         # if length of results is more than 1
# #         # then continue filtering
# #         # otherwise give the response
# #         replies[message.chat.id] = { filter: "Colour", data: colour }
# #         bot.send_message(message.chat.id, "is it Large?")
# #       # else:
# #       #   bot.send_message(message.chat.id, f"Is it a {}")

# #   if response == 'No':
# #   # Filter the data accordingly.
# #     item_type = data[data['Type'] == 'Vegetable']
# #     print(item_type)
# #     replies[message.chat.id] = {filter:"Type", data:item_type}
# #     bot.send_message(message.chat.id, "is it Green?")
# #     #bot.reply_to(message, message.text)
# #   elif response == 'Yes': 
# #     item_type = data[data['Type'] == 'Animal'] 
# #     print(item_type)
# #     replies[message.chat.id] = {filter:"Type", data:item_type}
# #     bot.send_message(message.chat.id, "is it Green?")
# # # #filter through the csv file if it is an animal, filter by animal. 
    
