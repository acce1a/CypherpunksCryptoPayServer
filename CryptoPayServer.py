from BtcTransactionProcessor import BtcTransactionProcessor as BTP
from Database import Database
from User import User
import threading
import qrcode

FILE_TO_STORE_THE_FUNDS = ''

class CryptoPayServer(object):
    def __init__(self):
        self.db = Database()
        x = threading.Thread(target=BTP.wait4payment, args=(self.db,))
        x.start()
    
    def newuser(self, arg):
        """
        Recebe como argumento um dict com as chaves name, email, description e pgp_key.
        Retorna a o endereço da wallet e abre uma thead para esperar o pagamento
        """
        nuser = User(arg['name'], arg['email'], arg['description'], arg['pgp_key'])
        self.db.insert(user.get_dict())

        return (nuser.addr, self.gen_qrcode(nuser.addr))

    @staticmethod
    def is_in_time(start):
        now = time.time()
        hours, rem = divmod(now-start, 3600)
        if int(hours) > 24:
            return False
        else:
            return True
    
    def wait4payment(self):
        while True:
            for user in self.db.get_unpaid_users():
                if BTP.is_in_time(user.time) and BTP.is_payment_received(user.addr):
                    user.paid = True
                    self.db.insert(user.get_dict())
                    with open(FILE_TO_STORE_THE_FUNDS, 'a') as f:
                        f.write('\n{}'.format(user.privkey))
                else:
                    if BTP.balance(user.addr) > 0:
                        with open(FILE_TO_STORE_THE_FUNDS, 'a') as f:
                            f.write('\n{}'.format(user.privkey))
                    self.db.remove('pgp_key', user.pgp_key)

    def gen_qrcode(self, addr):
        qr = qrcode.QRCode(version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10, border=4,)
    
        qr.add_data('Some data')
        qr.make(fit=True)

        return qr.make_image(fill_color="black", back_color="white")