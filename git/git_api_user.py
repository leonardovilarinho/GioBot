from httpx import get
from ranking import ranking


def get_info(user):
    res = get(f"https://api.github.com/users/{user}").json()
    msg = f"{res['name']}\n Repos: {res['public_repos']}\n  {res['html_url']} \n Gits: {res['public_gists']}\n  Seguidores: {res['followers']}\n Seguindo: {res['following']}\n {res['blog']}\n :information_source: {res['bio']} \n {res['location']}"
    ranking.write_db(res["login"], res["public_repos"])
    return msg
