# this is becuz we do not want anyone that looks into the script to know the api key
import os
import telebot
import numpy as np
import pandas as pd

# creating the bot instance
bot = telebot.TeleBot('API KEY HERE ', parse_mode=None)


# This is the first command that starts the bot
@bot.message_handler(commands=['start', "hello"])
def send_welcome(message):
    bot.reply_to(message, "hello, how are you doing?")


# the help command to give the user some form of guidance
@bot.message_handler(commands=['help'])
def help_bar(message):
    bot.reply_to(message, "this bot is a machine learning bot.")  # working


# this message will not reply the users previous massage it will instead send a message to the user
@bot.message_handler(commands=['hi'])
def hi_chat_id(message):
    bot.send_message(message.chat.id, "hi, good to see you ")


# just added it for kicks but maybe the bot can also log the user out
@bot.message_handler(commands=['Bye'])
def hi_chat_id(message):
    bot.reply_to(message, " Bye \n See you again ")


# This is the machine learning part. the main function of the bot this next line collects input from the user
@bot.message_handler(content_types=['text'], commands=["predict"])
def pred(message):
    sent_msg = bot.send_message(message.chat.id,
                                "please input the amount of years that you wish to see the predicted salary")
    bot.register_next_step_handler(sent_msg, predict_handler)


# this is the machine learning algorithm i have a small but clean dataset that i use to make this predictions
def predict_handler(message):
    predict = message.text
    bot.send_message(message.chat.id, f"the amount of years requested is  {predict}. ")
    test = predict

    # importing the dataset
    data_frame = pd.read_csv("Salaries.csv")
    X = data_frame.iloc[:, 0:1].values
    Y = data_frame.iloc[:, -1].values

    # now to feed the machine learning model we are using the linear regression
    from sklearn.linear_model import LinearRegression
    regress = LinearRegression()
    regress.fit(X, Y)
    # now for it to predict the salaries for the x_test data we wil save it into y_pred
    test = np.array(test)
    test = test.reshape(1, -1)
    Y_pred = regress.predict(test)
    Y_pred = int(Y_pred)
    bot.send_message(message.chat.id, f"the salary of a person of {predict} years of Experience is ${Y_pred}")

#Metro,Mmadafaka and co 2022/2023
bot.polling()
