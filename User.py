from BtcTransactionProcessor import BtcTransactionProcessor

class User(object):
    def __init__(self, name, email, description, pgp_key):
        self.name = name
        self.email = email
        self.description = description
        self.pgp_key = pgp_key
        self.paid = False
        self.privkey, self.addr = BtcTransactionProcessor.gen_wallet()        
    
    def get_dict(self):
        d = {'name': self.name,
        'paid': self.paid,
        'addr': self.addr,
        'privkey': self.privkey,
        'email': self.email,
        'description': self.description,
        'pgp_key': self.pgp_key
        }

        return d