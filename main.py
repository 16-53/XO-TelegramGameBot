from telebot import TeleBot
from pathlib import Path

token = Path("token.txt").read_text().strip()
bot = TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_game(chat_id=message.chat.id, game_short_name='XO_Game')


@bot.callback_query_handler(func=lambda callback_query: callback_query.game_short_name == 'XO_Game')
def game(call):
    bot.answer_callback_query(callback_query_id=call.id, url='https://playtictactoe.org/')


bot.polling(none_stop=True, interval=0)
