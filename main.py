import os
import telebot
import csv

with open('Addendum.csv', 'r') as data:
  csv_file = csv.reader(data)

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

#filter through the csv file if it is an animal, filter by animal. 
    
bot.polling()