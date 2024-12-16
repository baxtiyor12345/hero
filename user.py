from card import Card

class User(Card):
    def __init__(self,name,surname,bag,admin):
        super().__init__()
        self.name = name
        self.surname = surname
        self.bag = bag
        self.admin = admin
