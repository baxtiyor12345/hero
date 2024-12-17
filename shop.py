from product import Product
class Shop:
    def __init__(self,title,location,balance):
        self.title = title
        self.location = location
        self.clients = []
        self.products = []
        self.balance = balance
        self.history_sell = []

    def product_list(self):
        for item in self.products:
            if isinstance(item,Product):
                print(f"{item.name} -- muddati:{item.date_use} , Narxi: {item.cost}")
    def user_register(self):
        user_id = input("User ID ni kiriting: ")
        if user_id.isdigit():
            for client in self.clients:
                if client.user_id == int(user_id):
                    print("Tabriklaymiz,Tizmimizda mavjud ekansiz Do'kondan mahsulotlar xarid qilishingiz mumkin. ")
            else:
                print("Tizimda bunday ID li mijoz yo'q yoki kiritilgan ID xato.Iltimios to'g'ri ID kiriting yoki Ro'yxatdan o'ting. ")
        else:
            print("User ID si faqat sonlarda kiritishi kerak. ")

