# Вопрос 1 
# ООП - это обекно оринтированная програмирования/парадигма.ООП было создана для оринтации в кодах корорые мы пишем.
# ООП подраздилают на

# Классы - Шаблоны
# Обекты - Екземпляры

# основные Концепции ООП
# 1.Полиморфизм
# 2.Инкапсуляция 
# 3.Наследования
# 4.Обстракция

# solved:

# Вопрос 2
# сеттер и Геттер и есть 'Proprtie' это методы которые создаются програмистами для получение данных которые могут быть инкапсулированы
# с помошю сетер мы можем вызвать данное хранилише которое также могло быть личным и поменять ее данные 
# и вывести в терминаль/консоль сс помошю употреблени метода геттер 
# solved:

# Вопрос 3



# В классе существуют несколько типов переменных и методов
# Локальные переменные:

# Это переменные, объявленные внутри метода класса. Они доступны только в рамках этого метода.
# Переменные экземпляра (атрибуты экземпляра):

# Это переменные, связанные с конкретным экземпляром класса. Они объявляются внутри методов, как правило, в конструкторе __init__ с использованием self.

# Методы 
# Обычные методы:

# Методы, которые работают с переменными экземпляра. Для их вызова требуется создать экземпляр класса. Они принимают первым параметром self, который ссылается на текущий экземпляр класса.

# Методы класса:

# Эти методы работают с переменными класса и принимают первым аргументом cls, который ссылается на сам класс, а не на конкретный экземпляр. Для их объявления используется декоратор @classmethod.





# Вопрос 4
# Конструктора в ООП бывет -> __init__ and __new__ которые нужны для создании новых обектов 
# Итак __init__ это конструкттор кторый срабатывет при создании нового обекта в ООП 
# __new__ - это конструктор который создает данные новые обекты 

# Что касаема destructor то это опосайд сторона конструктов что собственно и значить что если 
# конструктора создаеют новые обекты где в далнейшем будут хранится данные то деструктор будет удалять их или унечтожать 

# Вопрос 5
# Глобальными переменными являюются переменные которые доступны во всех строках кода и могут быть употреблены везде
# локальные переменные могут быть созданы внутри методов и не могут быть употреблены вне метода 
# А нонлокал переменные доступны 2 и болле методом не являясь глабальными 
# solved:















# Task1
# x = int(input("From = "))
# y = int(input("To = "))

# for num in range(x, y + 1):
#     for i in range(1, 11):
#         print(f"{num} x {i} = {num * i}")
#     print()

        

# solved:


# Task2
# class Cyrcle:
#     PI = 3.14
   
#     def __init__ (self,radius):
#         self.radius = radius
    
#     def get_area (self):
#         return f"area = {2 * self.PI * self.radius ** 2}"

#     def get_diametr (self):
#         return f"diametr = {2 * self.radius}" 
    
#     def get_cyrcumference (self):
#         return f"cyrcumfrence = {2 * self.PI * self.radius}"
    
#     def get_radius (self):
#         return f"radius = {self.radius}"
    
# obj1 = Cyrcle(2)
# print(obj1.get_area())
# print(obj1.get_diametr())
# print(obj1.get_cyrcumference())
# print(obj1.get_radius())
# solved:


# Task3
# import math

# class Calculator:
    
#     @staticmethod
#     def factorial(n):
#         return math.factorial(n)
    
#     @staticmethod
#     def power(a, b):
#         return a ** b
    
#     @staticmethod
#     def sqrt(n):
#         return math.sqrt(n)

# print("Factorial of 5:", Calculator.factorial(5))
# print("2 to the power of 3:", Calculator.power(2, 3))
# print("Square of 16:", Calculator.sqrt(16))

# aolved:





# Task4

# class Calsculator:
#     def __init__(self,first_number,second_number):
#         self.firsnumber = first_number
#         self.secondnumber = second_number

# class CalculatorManager (Calsculator):
#     pass 
    
#     def sum (self):
#         return f"{self.firsnumber} + {self.secondnumber} = {self.firsnumber + self.secondnumber}"
#     def Substract (self):
#         return f"{self.firsnumber} - {self.secondnumber} = {self.firsnumber - self.secondnumber}"
#     def multiplication (self):
#         return f"{self.firsnumber} * {self.secondnumber} = {self.firsnumber * self.secondnumber}"
#     def devision (self):
#         return f"{self.firsnumber} / {self.secondnumber} = {self.firsnumber / self.secondnumber}"
    

# print("\nWelcome to calculator made by oop paradigma!")
# while True:
#     obj1 = CalculatorManager(int(input("Enter the first number: ")),int(input("Enter the second number: ")))
    
#     user_input = input("\n1.Sum + \n2.substract - \n3.multiplication * \n4.devision / \nSelect an option -> ")
#     if user_input == '1':
#         print(obj1.sum())
#     if user_input == '2':
#         print(obj1.Substract())
#     if user_input == '3':
#         print(obj1.multiplication())
#     if user_input == '4':
#         print(obj1.devision())
# solved:
   
# Task 5 

# class Students:
#     def __init__ (self,name,username,age,idd):
#         self.name = name
#         self.age = age
#         self.username = username
#         self.idd = idd
# database = []
# class Students_manager (Students):
#     pass

#     def eccept (self):
#         new_student = Students(
#             input("Enter ur name: "),
#             input("Enter ur age: "),
#             input("Enter ur username "),
#             self.idd += idd
#         )
#         database.append(new_student)

#     def display (self):
#         for student in database:
#             print student        
