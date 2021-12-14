import os
import telebot
import pandas as pd

data = pd.read_csv('Addendum.csv')
replies = []

API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Greet'])
def greet(message):
  bot.reply_to(message, "Hey! Hows it going?")

@bot.message_handler(commands=['Hello'])
def hello(message):
  bot.send_message(message.chat.id, "Hello!")

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
    data1 = data[(data.Type=="Animal")]
    print("It worked")
    print(data1)
  @bot.message_handler(func=lambda message: True)
  def query2(message):
    bot.send_message(message.chat.id,"Is it large?")
    print(replies)
    data2 = data1[(data.Size=="Large")]
    if len(data2.index) == 1:
      ans = data2.iloc[0].Item
      print(ans)
      bot.send_message(message.chat.id, ans)
  query2(message)

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
    
bot.polling()