class Card:
    def __init__(self,number,password,datework,balance):
        self.number = []
        self.password = password
        self.datework = datework
        self.balance = 0

    def info(self):
        return f"{self.number,self.password,self.datework,self.balance}"