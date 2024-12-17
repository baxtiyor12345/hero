from shop import Shop
from user import User
from card import Card
from product import Product

shop = Shop("HUMO","Toshkent Shahar",10000)

user1 = User(12345678,"Akbarxon Fayzullayev","akbarxonfayzullayev@gmail.com","+998788889886",True)
user2 = User(87654321,"Kamoliddin Kabulov","kamoliddinkabulov@gmail.com","+998788889888",True)
user3 = User(11223344,"Ali Valiyev","alivaliyev@gmail.com","+998788889888",False)
user4 = User(44332211,"Nizomiddin Jamolov","nizomiddin@gmail.com","+998788889888",False)
user5 = User(12341234,"Alisher Navoiy","navoiylegenda@gmail.com","+998788889888",False)

card1 = Card(11111111,1111,1125)
card2 = Card(22222222,2222,1125)
card3 = Card(33333333,3333,1125)
card4 = Card(44444444,4444,1125)
card5 = Card(55555555,5555,1125)

user1.cards.append(card1)
user2.cards.append(card2)
user3.cards.append(card3)
user4.cards.append(card4)
user5.cards.append(card5)

shop.clients.append(user1)
shop.clients.append(user2)
shop.clients.append(user3)
shop.clients.append(user4)
shop.clients.append(user5)

product1 = Product("Olma",100,1929,5)
product2 = Product("Olcha",100,1929,6)
product3 = Product("Anor",100,1929,6)
product4 = Product("Nok",100,1929,6)
product5 = Product("Anjir",100,1929,5)
product6 = Product("Kiwi",100,1929,8)
product7 = Product("Uzum",100,1929,6)
product8 = Product("Apelsin",100,1929,8)
product9 = Product("Limon",100,1929,4)
product10 = Product("Xurmo",100,1929,7)

shop.products.append(product1)
shop.products.append(product2)
shop.products.append(product3)
shop.products.append(product4)
shop.products.append(product5)
shop.products.append(product6)
shop.products.append(product7)
shop.products.append(product8)
shop.products.append(product9)
shop.products.append(product10)

