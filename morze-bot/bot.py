from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler

alph = {
    'a': '·−',
    'b': '−···',
    'c': '−·−·',
    'd': '−··',
    'e': '·',
    'f': '··−·',
    'g': '−−·',
    'h': '····',
    'i': '··',
    'j': '·−−−',
    'k': '−·−',
    'l': '·−··',
    'm': '−−',
    'n': '−·',
    'o': '−−−',
    'p': '·−−·',
    'q': '−−·−',
    'r': '·−·',
    's': '···',
    't': '−',
    'u': '··−',
    'v': '···−',
    'w': '·−−',
    'x': '−··−',
    'y': '−·−−',
    'z': '−−··',
}

ralph = {alph[n]:n for n in alph}

updater = Updater(token='361546159:AAHtvJ3sfNAenziSe7VvaH5sZf1iCr9pnSA')

dispatcher = updater.dispatcher

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def inline_caps(bot, event):
    input = event.inline_query.query
    if not input: return

    input = input.lower()
    encoded = ''.join((alph[n] + ' ' if n in alph else n) for n in input)

    results = [
        InlineQueryResultArticle(
            id=hash(encoded),
            title='to morze',
            input_message_content=InputTextMessageContent(encoded),
            description=encoded
        )
    ]

    if '·' in input or '−' in input:
        decoded = ''.join(ralph[w] if w in ralph else w for w in input.split(' '))

        results.append(
            InlineQueryResultArticle(
                id=hash(decoded),
                title='from morze',
                input_message_content=InputTextMessageContent(decoded),
                description=decoded
            )
        )

    bot.answerInlineQuery(event.inline_query.id, results)


inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

print('Start polling')
updater.start_polling()
