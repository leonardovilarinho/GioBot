import ast

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("./giobot-telegram-firebase.json")
firebase_admin = firebase_admin.initialize_app(
    cred, {"databaseURL": "https://giobot-telegram.firebaseio.com/"}
)
ref = db.reference("ranking")


def write_db(git, repos):
    ref.child(git).set({"git": git, "repos": repos})


write_db("devgiordane", 15)


# def read_db():
#     with open("ranking/db.txt", "r", encoding="utf-8") as db:
#         ranking = ast.literal_eval(db.read())
#     return ranking


def gen_ranking():
    ranking = ref.get()
    lista = sorted(ranking.values(), key=lambda x: x["repos"], reverse=True)
    msg = ""
    for i, user in enumerate(lista):
        if i < 10:
            msg += f'{i+1}º {user["git"]} com {user["repos"]} repos \n'
    return msg
