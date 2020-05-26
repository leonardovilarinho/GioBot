from sqlite3 import connect
from random import randint
from httpx import get


def gen_charada():
    headers = {"Accept": "application/json"}
    res = get(
        "https://us-central1-kivson.cloudfunctions.net/charada-aleatoria",
        headers=headers,
    ).json()
    return res


def gen_charadax():
    with connect("database.sqlite") as db:
        cursor = db.cursor()
        n = randint(1, 1816)
        query = cursor.execute(f"select pergunta from charadas where id={n}")
    return f"ID da sua charada: {n}\n{query.fetchone()[0]}"


def resposta_charadax(id):
    with connect("database.sqlite") as db:
        cursor = db.cursor()
        query = cursor.execute(f"select resposta from charadas where id={id}")
    return f"{query.fetchone()[0]}"
