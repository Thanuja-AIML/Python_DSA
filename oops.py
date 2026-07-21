# 4 pillars of OOPS
# Encapsulation 
# access modifiers
# class A:
#     def __init__(self,name,age,gender):
#     #constructor
#         self.__name=name#private variable ca be accessed inside of same class which defines with __
#         self.age=age#protected variable  can be accessed inside of same
#         self.gender=gender#public variable can be accessed inside of same class and outside of all classes which defines with no prefix
#     def display(self):
#         print(self.__name)
#         print(self._age)
#         print(self.gender)
# a1=A("thanuja",20,"female")
# a2=A("varshi",20,"female")
# # print(a1.__name)
# print(a2._age)
# print(a2.gender)
    
    
    
# Abstraction
# from abc import ABC,abstractmethod
# class BankAccount(ABC):
#     def __init__(self,balance):
#         self.__balance=balance
#     def deposit(self,amount):
#         self.__balance+=amount
#     def withdraw(self,amount):
#         self.__balance-=amount
#     def getBalance(self):
#         return self.__balance
#     @abstractmethod
#     def interestcalc(self):
#         pass
# class SavingAccount(BankAccount):
#     def interestcalc(self):
#         return self.__balance*0.05




    
# Inheritance


# Polymorphism
class Animal:
    print("animal sound")
class Dog(Animal):
    def sound(self):
        print("Woof")
class Cat(Animal):
    def sound(self):
        print("Meow")