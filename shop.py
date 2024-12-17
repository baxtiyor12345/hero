class Shop:
    def __init__(self,title,location,balance):
        self.title = title
        self.location = location
        self.clients = []
        self.balance = balance
        self.history_sell = []
