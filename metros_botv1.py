import os
import telebot
import numpy as np
import pandas as pd
import time

# creating the bot instance
bot = telebot.TeleBot('API KEY ', parse_mode=None)


@bot.message_handler(commands=['start',"hello"])
def send_welcome(message):
    bot.reply_to(message, "hello, how are you doing?")
    # to show the amount of pple that are using the bot i would have added time but my hosting does not have large space


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.reply_to(message,
                 "This is a machine learning  bot. \n LISTS OF COMMANDS \n /predict_salary - To Predict Salaries With "
                 "Years Of Experience In The IT Industry \n /developers_niche - for those who sre interested in "
                 "seeing the code behind the bot ")


@bot.message_handler(commands=['developers_niche'])
def check_code(message):
    bot.reply_to(message,
                 "Oh, you are curious to see how my gears work \n well visit \n  "
                 "https://github.com/metrosmash/Metros_Bots ")


@bot.message_handler(commands=['hi'])
def hi_chat_id(message):
    bot.send_message(message.chat.id, "hi, good to see you ")


@bot.message_handler(commands=['Bye'])
def hi_chat_id(message):
    bot.reply_to(message, " Bye \n See you again ")


@bot.message_handler(content_types=['text'], commands=["predict_salary"])
def pred(message):
    sent_msg = bot.send_message(message.chat.id,
                                "please input the amount of years that you wish to see the predicted salary")
    bot.register_next_step_handler(sent_msg, predict_handler)


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


@bot.message_handler(content_types=['text'], commands=["feedback"])  # check
def feedback(message):
    sent_msg = bot.send_message(message.chat.id,
                                "what are your feedbacks, what do you feel is not right or how was your experience "
                                "with the bot ?")
    bot.register_next_step_handler(sent_msg, feedback_handler)


def feedback_handler(message):
    feed_back = message.text
    file = open("bot_log.txt", "a")
    file.write(feed_back)
    file.write("\n")
    file.close()
    bot.send_message(message.chat.id, "Your Feedback Has Been Saved ")


while True:
    try:
        bot.polling()
    except:
        time.sleep(15)

# Metro,Mmadafaka and co 2022/2023
