""" 1 """
""" Инкапсуляция """
# Инкапсуляция, наследование и полиморфизм являются принципами ООП(также туда можно отнести абстракцию).
# Инкапсуляция - механизм, при котором внутренние детали реализации объекта остаются скрытыми, а взаимодействие с ним осуществляется через специально определённый интерфейс.
# Пример

#
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # приватный атрибут

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#     def get_balance(self):
#         return self.__balance


# account = BankAccount(100)
# account.deposit(50)
# print(account.get_balance())
#

""" Наследование """
# Механизм, который позволяет на основе существующих классов (родительских), создавать новые классы (дочерние).
# Атрибуты и методы родительских классов переиспользуются в дочерних.
# Пример

#
# from datetime import datetime


# class Store:
#     def __init__(self, address):
#         self.address = address

#     def is_open(self, date):
#         return False

#     def get_info(self, date_str):
#         try:
#             date_object = datetime.strptime(date_str, '%d.%m.%Y')
#         except ValueError:
#             return f'Некорректный формат даты: {date_str}'

#         if self.is_open(date_object):
#             info = 'работает'
#         else:
#             info = 'не работает'
#         return f'Магазин по адресу {self.address} {date_str} {info}'


# class MiniStore(Store):
#     def is_open(self, date):
#         return date.weekday() in (0, 1, 2, 3, 4)


# class WeekendStore(Store):
#     def is_open(self, date):
#         return date.weekday() in (5, 6)


# class NonStopStore(Store):
#     def is_open(self, date):
#         return True


# mini_store = MiniStore('Улица Немига, 57')
# print(mini_store.get_info('29.03.2024'))
# print(mini_store.get_info('30.03.2024'))
# weekend_store = WeekendStore('Улица Толе би, 321')
# print(weekend_store.get_info('29.03.2024'))
# print(weekend_store.get_info('30.03.2024'))
# non_stop_store = NonStopStore('Улица Арбат, 60')
# print(non_stop_store.get_info('29.03.2024'))
# print(non_stop_store.get_info('30.03.2024'))
#

""" Полиморфизм """
# Атрибуты и методы иногда называют интерфейсом класса. 
# Переопределение методов позволяет сохранить интерфейс класса, изменив поведение его методов и значения атрибутов.
# Такое переопределение методов и атрибутов является проявлением полиморфизма
# Пример

#
# class Cat:
#     def speak(self):
#         print("Cat says meow")

# class Dog:
#     def speak(self):
#         print("Dog says woof")

# def make_animal_speak(animal):
#     animal.speak()

# cat = Cat()
# dog = Dog()

# make_animal_speak(cat)
# make_animal_speak(dog)
#

""" 2 """

# прежде всего нужно посмотреть нужный нам коммит. 
# git log
# Затем есть несколько путей:
# 1) сохраняет изменения в рабочем каталоге
# git reset --soft <commit_hash>
# 2) с удалением изменений
# git reset --hard <commit_hash>
# 3) отмена последнего коммита
# git reset --hard HEAD^

""" 3 """

# def is_palindrome(s):
#     s = s.lower().replace(" ", "")
#     return s == s[::-1]  

# print(is_palindrome("АзОзА"))

""" 4 """

# Ещё с 9 класса увлёкся программированием. После 9 поступил в Высший колледж информатики(НГУ).
# На втором курсе прошёл интенсив школы21(сбер) (успешно). 
# Работал преподователем Python в летней школе.
# На данный момент на 4 курсе. Изучаю курсы от Yandex-практикум. Python-разработчик.

# Могу рассказать ещё многое на собеседование.
# Спасибо, что уделили время и внимание мне и моим проектам.
# Ссылка на github: https://github.com/Almedada?tab=repositories