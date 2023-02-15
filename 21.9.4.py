# Команда проекта «Дом питомца» планирует большой корпоратив для своих клиентов.
# Вам необходимо написать программу, которая позволит составить список гостей.
# В класс «Клиент» добавьте метод, который будет возвращать информацию только об имени, фамилии и городе клиента.
#
# Затем создайте список, в который будут добавлены все клиенты, и выведете его в консоль.

class Client:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city

    def get_clients(self):
        return (f'{self.name} {self.surname}. {self.city}.')

client1 = Client('Иван', 'Петров', 'Москва')
client2 = Client ('Полина', 'Вершинина', 'Ясенево')
all_clients = [client1, client2]

for guest in all_clients:
    print(guest.get_clients())


