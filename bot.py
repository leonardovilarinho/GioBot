from telegram.ext import Updater, CommandHandler
from token_api import token_api, yt_key
from httpx import get

from sqlite3 import connect
from random import randint

db = connect('database.sqlite')


cursor = db.cursor()


def charada(update, context):
    n = randint(1, 1816)
    query = cursor.execute(f'select pergunta from charadas where id={n}')
    return f"""
    ID da sua charada: {n}

    {query.fetchone()[0]}
    """


def resposta_charada(update, context):
    query = cursor.execute(
        f'select resposta from charadas where id={context.args[0]}'
    )
    return query.fetchone()[0]


def git_api_user(user):
    res = get(f"https://api.github.com/users/{user}").json()
    msg = f"{res['name']}\n Repos: {res['public_repos']}\n  {res['html_url']} \n Gits: {res['public_gists']}\n  Seguidores: {res['followers']}\n Seguindo: {res['following']}\n {res['blog']}\n :information_source: {res['bio']} \n {res['location']}"
    return msg


def yt_api_subs():
    url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCANI94YmcIGmabIDPx5oHYg&fields=items/statistics/subscriberCount&key={yt_key}"
    res = get(url).json()
    msg = f"Opa Dev_, já somos mais de {res['items'][0]['statistics']['subscriberCount']}\nMuito obrigado por fazer parte disso <3"
    return msg


def hello(update, context):
    update.message.reply_text(
        "Hello {}".format(update.message.from_user.first_name)
    )


def get_git_user(update, context):
    update.message.reply_text(git_api_user(context.args[0]))


def get_yt_subs(update, context):
    update.message.reply_text(yt_api_subs())


# /git devgiordane

updater = Updater(token_api, use_context=True)

updater.dispatcher.add_handler(CommandHandler("hello", hello))
updater.dispatcher.add_handler(CommandHandler("git", get_git_user))
updater.dispatcher.add_handler(CommandHandler("subs", get_yt_subs))
updater.dispatcher.add_handler(CommandHandler("charada", charada))
updater.dispatcher.add_handler(CommandHandler("resposta", resposta_charada))

updater.start_polling()
updater.idle()
