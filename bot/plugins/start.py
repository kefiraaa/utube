from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

def start(bot, update):
    update.message.reply_text('Привет! Я информационный бот компании "Путешествия и туризм".\n'
                              'Для получения информации можете воспользоваться подсказками ниже!',
                              reply_markup=markup)

def close_keyboard(bot, update):
    update.message.reply_text('Ok', reply_markup=ReplyKeyboardRemove())

def echo(bot, update):
    if update.message.text[-1] == '?':
        update.message.reply_text('Конечно можно спросить! Только я культурно промолчу...')
    else:
        update.message.reply_text('Вполне возможно, кто ж знает?')

def address(bot, update):
    update.message.reply_text('Адрес: Китай, Гималаи, хребет Махалангур-Химал, вершина Эверест, д. 1')

def phone(bot, update):
    update.message.reply_text('Телефон: +86 133 2686 8519')

def site(bot, update):
    update.message.reply_text('Сайт: https://yandex.ru/everest/')

def work_time(bot, update):
    update.message.reply_text('Время работы: пн-пт, 9-00 - 19-00')


updater = Updater('1214407282:AAE2HtWxWu1cwpB7sbYqZg913FnldHjOtfc')

dp = updater.dispatcher

reply_keyboard = [['/address', '/phone'],
                  ['/site', '/work_time']]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

dp.add_handler(CommandHandler('start', start))

dp.add_handler(CommandHandler('close', close_keyboard))

dp.add_handler(CommandHandler('address', address))
dp.add_handler(CommandHandler('phone', phone))
dp.add_handler(CommandHandler('site', site))
dp.add_handler(CommandHandler('work_time', work_time))

text_handler = MessageHandler(Filters.text, echo)
dp.add_handler(text_handler)

updater.start_polling()

updater.idle()