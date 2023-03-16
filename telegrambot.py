import telebot
from telebot import types

bot = telebot.TeleBot('5921328392:AAEerZ4GsaSfqRxHbTW8b7R0qYrBva4syGE')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Привет! Я твой бот-помошник!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Мій інстанрам')
        btn2 = types.KeyboardButton('Ютуб лєгєнди')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Інщі питання:', reply_markup=markup) #ответ бота


    elif message.text == 'Мій інстаграм':
        bot.send_message(message.from_user.id, 'Переходем по силочкі і підписуємся!!!' + '[ссылке](https://www.instagram.com/maxsim_laptev/)', parse_mode='Markdown')

    elif message.text == 'Ютуб лєгєнди':
        bot.send_message(message.from_user.id, 'Ти незнаєш шо за лєгєнда?Тоді бистро підписався!!!!' + '[ссылке](https://www.youtube.com/@Volga565)', parse_mode='Markdown')

bot.polling(none_stop=True, interval=0) #обязательная для работы бота частьrkup=markup) #ответ бота