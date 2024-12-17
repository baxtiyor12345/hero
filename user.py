import re

from card import Card

class User:
    user_list = []
    def __init__(self, user_id, surname,firstname, email, phone, admin,card):
        self.user_id = user_id
        self.surname = surname
        self.firstname = firstname
        self.email = email
        self.phone = phone
        self.cards = []
        self.basket = []
        self.admin = admin
        self.card = card

    @classmethod
    def registration(cls):
        firstname = str(input("Введите свое имя: "))
        surname = str(input("Введите свою фамилию: "))
        user_chosepasport_or_phone = int(input("Выберите что будете регестрировать и введите число одно:\n1.ВВедите паспорт айди. \n2.ВВести номер телефона.\n3.ВВести оба Паспорт айди и номер телефона. Также напоминание в случае двойной авторизации будет скидка 5% на первую покупку.\nВВедите свой выбор:  "))
        if user_chosepasport_or_phone == 1:
            user_id = str(input("Введите свой паспортный айди: "))
            phone = None  # телефон керемас
        if user_chosepasport_or_phone == 2:
            phone = int(input("Введите свой номер телефона: "))
            user_id = None  # айди керемас
        elif user_chosepasport_or_phone == 3:
            user_id = str(input("Введите свой паспортный айди: "))
            phone = int(input("Введите свой номер телефона: "))
        else:
            return print("Введите цифру одну.")

        email = str(input("Введите свой эмаил:"))
        cards = int(input("Введите свои карты"))

    @classmethod
    def show_users(cls):
        if not cls.user_list:
            print("Нет зарегистрированных пользователей.")
        else:
            for user in cls.user_list:
                print(
                    f"ID: {user.user_id}, Имя: {user.firstname} {user.surname}, Почта: {user.email}, Телефон: {user.phone}, Карта: {user.cards}, Админ: {user.admin}")

User.registration()
User.show_users()

def user_menu(self):
        user_inp = int(input("Выберите товар"))

def admin_menu(self):
        pass

#
# def get_admins():
#         if superuser.admin:
#             return admin_menu()
#         else:
#             return user_menu()
