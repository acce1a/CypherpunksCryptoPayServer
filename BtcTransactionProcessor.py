from pycoingecko import CoinGeckoAPI
import time
import requests
import pybtc

PRICE = 0.0001 # preço em BTC por chave publicada

class BtcTransactionProcessor(object):
    @staticmethod
    def is_payment_received(addr):
        return balance(addr) <= PRICE
    
    @staticmethod
    def gen_wallet():
        a = pybtc.Address()
        privkey = a.private_key.wif
        pubkey = a.address

        return (privkey, pubkey)
    
    @staticmethod
    def balance(addr):
        req = requests.get('https://blockexplorer.com/api/addr/{}'.format(addr))
        data = json.loads(req.text)

        return data['balance']

    @staticmethod
    def get_curret_price():
        data = CoinGeckoAPI().get_price(
            ids='bitcoin',
            vs_currencies='brl')

        price ={'crypto': 'bitcoin',
                'fiat': 'brl',
                'price': data['bitcoin']['brl'], 
                'time': time.localtime(time.time())}
        
        return price
