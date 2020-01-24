from BtcTransactionProcessor import BtcTransactionProcessor
from Database import Database
from User import User

import threading

FILE_TO_STORE_THE_FUNDS = ''

class CryptoPayServer(object):
    def __init__(self):
        self.db = Database()

    def new_user_request(self, user):
        self.db.insert(user.get_dict())
    
    def loop_wait4payment(self, user):
        if BtcTransactionProcessor.is_payment_received(user.addr):
            user.paid = True
            self.db.insert(user.get_dict())
            with open(FILE_TO_STORE_THE_FUNDS, 'a') as f:
                f.write('\n{}'.format(user.privkey))
    
    def newuser(self, arg):
        """
        Recebe como argumento um dict com as chaves name, email, description e pgp_key.
        Retorna a o endereço da wallet e abre uma thead para esperar o pagamento
        """
        nuser = User(arg['name'], arg['email'], arg['description'], arg['pgp_key'])

        x = threading.Thread(target=self.loop_wait4payment, args=(nuser,))
        x.start()

        return nuser.addr
