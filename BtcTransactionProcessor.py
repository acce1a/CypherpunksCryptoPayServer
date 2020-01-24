from pycoingecko import CoinGeckoAPI
import time
import requests
import pybtc

PRICE = 0.0001 # preço em BTC por chave publicada

class BtcTransactionProcessor(object):
    @staticmethod
    def is_payment_received(addr):
        # A day has 86400 seconds
        MAX = 86400
        count= 0
        while self.balance(addr) <= PRICE:
            time.sleep(3)
            count+=3
            if count >= MAX:
                return False
        else:
            return True
    
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
