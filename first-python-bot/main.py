from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent

updater = Updater(token='374530671:AAE0Q-_ADjQZv30lOjVB4-sPE6C0ZJtb3Hs')

dispatcher = updater.dispatcher

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

users_count = 0

jokes = [
    """
    Она: ответь мне, только честно, да или нет, хорошо?
    Он: спрашивай
    Она: почему мужчины смеются над блондинками?
    Он: да
    """,

    """
    111: ппц, сижу ржу дома, не могу успокоиться))
    222: чего там?
    111: короче стою сегодня курю около метро, после универа.ко мне подходит поцан и спрашивает спички. а я как раз утром из дома коробок прихватил. ну я ни слова не говорю, вытаскиваю из кармана, протягиваю.
    222: ))
    111: он так смотрит, грит, зажигалкой то удобнее
    111: я опять же молча лезу в тот же карман и достаю крикет
    111: он прикуривает, отдает зажигалку, смотрит на меня секунд десять и говорит типо в шутку какой карман удивительный, все что не попросишь, все есть, небось и конфеты есть
    222: тааак, я начинаю догадываться)
    111: ))))не поверишь, уже неделю ношу с собой несколько бон пари.
    111: я молча достаю из того же кармана леденец, он ошарашенно берет его, его глаза полны ужаса
    222: ппц, бедняга))
    111: после этого я говорю ему "ты потратил все три своих желания", выкидываю сигарету, разворачиваюсь и ухожу
    """,

    """
    ГламуРрКа: ПрИвЕтИк
    ATM: Чё надо?
    ГламуРрКа: Ты ЧиВо ТаКаЯ БукА? =)))
    ATM: Иди нахуй
    ГламуРрКа: ЧеГоО?!?!?!
    ATM: ИдИ НаХуЙ
    """,

    """
    - Это Бля Агапова!
    - Здравствуй, Бля Агапова, хуле ты хотела?
    - Ой, простите, Елена Вячеславовна, я вместо "Ю" нечаянно "Б" поставила... :-[
    - Да ничего страшного, я в слове "что" тоже опечаталась...
    """,

    """
    <@ghoul> мы попали на баш орг :-)
    <Sevan> да я вот вчера и видел
    <Sevan> с пробелами
    <Sevan> главное сначал прочел, думаю во два дибила, потом ники посмотрел :-)))))))
    """,

    """
    <Nub> Кто-нибудь может объяснить, как делятся клетки?
    <K4rli> o
    <K4rli> 0
    <K4rli> 8
    <K4rli> oo
    """
]


def is_prime(n):
    pass



# generate plural form of n in russian
def plural_form(n):
    if n % 10 in [0, 1, 4, 5, 9]:
        return 'ый'

    if n % 10 == 3:
        return 'ый' if n % 100 == 13 else 'ий'

    # 2, 6, 7, 8
    return 'ый' if n // 10 % 10 == 1 else 'ой'


def start(bot, update):
    global users_count
    users_count += 1
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Ты " + str(users_count) + str(plural_form(users_count)) + ", Нео")


import random


def joke(bot, event):
    global jokes

    chat = event.message.chat
    print([chat.username, chat.first_name, chat.last_name])

    num = random.randint(0, len(jokes))
    bot.sendMessage(chat_id=chat.id, text=jokes[num])


def echo(bot, event):
    bot.sendMessage(chat_id=event.message.chat_id, text=event.message.text[::-1])


def no_photo(bot, event):
    bot.sendMessage(chat_id=event.message.chat_id, text='Фоточки не понимаю, сорян')


def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)


def inline_caps(bot, event):
    query = event.inline_query.query
    if not query: return

    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        ))

    bot.answerInlineQuery(event.inline_query.id, results)


inline_caps_handler = InlineQueryHandler(inline_caps)
start_handler = CommandHandler('start', start)
joke_handler = CommandHandler('joke', joke)
caps_handler = CommandHandler('caps', caps, pass_args=True)
echo_handler = MessageHandler(Filters.text, echo)
no_photo_handler = MessageHandler(Filters.photo, no_photo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(joke_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(no_photo_handler)
dispatcher.add_handler(inline_caps_handler)

print('Start polling')
updater.start_polling()
