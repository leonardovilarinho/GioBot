from telegram.ext import Updater, CommandHandler
from time import sleep
from youtube_api import get_subs
from token_api import token_api, yt_key
from git import git_api_user
from charada import charada
from ranking import ranking


def hello(update, context):
    update.message.reply_text(
        f"Opa dev_ {update.message.from_user.first_name}, que legal te ver por aqui :)"
    )


def get_git_user(update, context):
    update.message.reply_text(git_api_user.get_info(context.args[0]))


def get_yt_subs(update, context):
    update.message.reply_text(get_subs.get_subs())


# TODO TORNAR O RANKING DINAMICO, E ATUALIZAR ELE, SEMPRE QUE O /GIT FOR CHAMADO
def get_ranking(update, context):
    update.message.reply_text(ranking.gen_ranking())


def get_charada(update, context):
    msg = charada.gen_charada()
    update.message.reply_text(msg["pergunta"])
    sleep(10)
    update.message.reply_text(msg["resposta"])


# def charada(update, context):
#     update.message.reply_text(gen_charadax())


# def res_charada(update, context):
#     update.message.reply_text(resposta_charada(context.args[0]))


updater = Updater(token_api, use_context=True)

# updater.dispatcher.add_handler(CommandHandler("charadax", charada))
# updater.dispatcher.add_handler(CommandHandler("resposta", res_charada))
updater.dispatcher.add_handler(CommandHandler("hello", hello))
updater.dispatcher.add_handler(CommandHandler("git", get_git_user))
updater.dispatcher.add_handler(CommandHandler("subs", get_yt_subs))
updater.dispatcher.add_handler(CommandHandler("charada", get_charada))
updater.dispatcher.add_handler(CommandHandler("ranking", get_ranking))

updater.start_polling()
updater.idle()
