class User:
    def __init__(self,user_id,fullname,email,phone,admin):
        self.user_id = user_id
        self.fullname = fullname
        self.email = email
        self.phone = phone
        self.cards = []
        self.basket = []
        self.admin = admin
