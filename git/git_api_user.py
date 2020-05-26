from httpx import get


def get_info(user):
    res = get(f"https://api.github.com/users/{user}").json()
    msg = f"{res['name']}\n Repos: {res['public_repos']}\n  {res['html_url']} \n Gits: {res['public_gists']}\n  Seguidores: {res['followers']}\n Seguindo: {res['following']}\n {res['blog']}\n :information_source: {res['bio']} \n {res['location']}"
    return msg
