import requests

def get_btc():
    url = 'https://yobit.net/api/2/btc_usd/ticker'
    r = requests.get(url).json()
    price = r['ticker']['last']
    return str(price) + ' usd'
