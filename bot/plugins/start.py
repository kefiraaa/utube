import telebot
from pyrogram import filters as Filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


token = '1912432053:AAHt2sGTDlkpc-KL8cYyZVuw-sauqEMRMl8'
bot = telebot.Telebot(token)

help = '/help'

from ..translations import Messages as tr
from ..config import Config
from ..utubebot import UtubeBot


@UtubeBot.on_message(
    Filters.private
    & Filters.incoming
    & Filters.user(Config.AUTH_USERS)
)
async def _start(c: UtubeBot, m: Message):
    await m.reply_chat_action("typing")

    await m.reply_text(
        text=tr.START_MSG.format(m.from_user.first_name),
        quote=True,
        keyboard = telebot.types.ReplyKeyboardMarkup(true)
        keyboard.row('Help')

        def send(id, text):
            bot.send_message(id, text, reply_markup = keyboard)

        @bot.message_handler(commands = ['start'])
        def answer(message):
            send(message.chat.id, 'Приветствую тебя!')

        @bot.message_handler(content_types = ['text'])
        def main(message):
            id = message.chat.id
            msg = message.text

            if msg == '/help':
                send(id.help)

            else:
                send(id, 'Я тебя не понял!')
          bot.polling(none_stop = True)
        ),
    )
