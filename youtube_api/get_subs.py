from httpx import get


def get_subs():
    url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCANI94YmcIGmabIDPx5oHYg&fields=items/statistics/subscriberCount&key={yt_key}"
    res = get(url).json()
    msg = f"Opa Dev_, já somos mais de {res['items'][0]['statistics']['subscriberCount']}\nMuito obrigado por fazer parte disso <3"
    return msg
