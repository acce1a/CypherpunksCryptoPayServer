from tinydb import TinyDB, Query

DBPATH = "keydatabase.json"

class Database(Object):
    def __init__(self):
        self.db = TinyDB(DBPATH)
        self.user = Query()
    
    def insert(self, form_dict):
        assert(isinstance(form_dict, dict), "Invalid data to insert in TinyDB")
        self.db.insert(form_dict)
        return True
    
    def remove(self, arg, var):
        assert(arg is in ['name','pgp_key','fingerprint'], "Arg {} don't exists".format(arg))

        if arg == 'name':
            self.db.remove(self.user.name == var)
        elif arg == 'pgp_key':
            self.db.remove(self.user.pgp_key == var)
        elif  arg == 'fingerprint':
            passself.db.remove(self.user.fingerprint == var)
        else:
            exit(-1)
        
        return True
    
    def get(self, arg, var):
        assert(arg is in ['name','pgp_key','fingerprint'], "Arg {} don't exists".format(arg))

        if arg == 'name':
            return self.db.search(self.user.name == var)
        elif arg == 'pgp_key':
            return self.db.search(self.user.pgp_key == var)
        elif  arg == 'fingerprint':
            return self.db.search(self.user.fingerprint == var)
        else:
            return False
        