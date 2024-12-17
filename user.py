from card import Card

class User:
    def __init__(self,namesurname,phone,cards,basket,role,passportId):
        self.namesurname = namesurname
        self.phone = phone
        self.basket = []
        self.role = role
        self.passportId = passportId
        self.cards = []
        # if self.basket == None:
        #    print("Пока нету продуктов")
        # else:
        #     print(self.basket)


    def info(self):
        return f"Имя пользователя и фамилия: {self.namesurname}\nНомер телефона: { self.phone}\n Айди пользователя: {self.passportId}\nПродукты в карзинепользовтеля: {self.basket}"

card1 = Card(8965420447844521,7346,"07/25",0)

user1 = User("Вира Кражевский",900368052,None,None,"User","AD0452765",)
user1.cards.append(card1)

print(user1.info())