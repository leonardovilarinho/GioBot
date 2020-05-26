import ast


def read_db():
    with open("ranking/db.txt", "r", encoding="utf-8") as db:
        ranking = ast.literal_eval(db.read())
    return ranking


ranking = read_db()


def gen_ranking():
    lista = sorted(ranking, key=lambda x: x["repos"], reverse=True)
    msg = ""
    for i, user in enumerate(lista):
        if i < 10:
            msg += f'{i+1}º {user["git"]} com {user["repos"]} repos \n'
    return msg
