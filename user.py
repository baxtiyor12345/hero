class User:
    def __init__(self,name,surname,passport_id,basket,admin):
        self.name = name
        self.surname = surname
        self.passport_id = passport_id
        self.cards = []
        self.basket = basket
        self.admin = admin
