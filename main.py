from bs4 import BeautifulSoup
import requests
import telebot

TOKEN = '2122652854:AAEiKduSrosdqfzNn5AEZy3AeDUn2XC06ew'

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')
welcome_text = '''
Здравствуйте, это новостной бот!
'''
url = 'https://24.kg/'


@bot.message_handler(content_types=['text'])
def handler(message):
    if message.text.lower() == 'привет':
        bot.reply_to(
            message=message, text=welcome_text
        )
    elif message.text.lower() == 'новости':
        source = requests.get(url)
        main_text = source.text
        soup = BeautifulSoup(main_text, "html.parser")
        news = [zs.text for zs in soup.find_all('div', {'class': 'one'})]
        bot.send_message(message.chat.id, news[:10])


bot.polling()
