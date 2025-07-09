# class Employee:
#     salary=100000 #class attributes
#     lang="py"

# t= Employee()
# t.name="tanu"
# print(t.name, t.salary, t.lang)

# r=Employee()
# r.name="robin" #instance attributes
# print(r.name, r.lang)


# instance vs class attributes
# class Employee:
#     salary=100000 #class attributes
#     lang="py"

# t= Employee()
# t.lang="JS"
# print( t.salary, t.lang)

# r=Employee()
# r.name="robin" #instance attributes
# print(r.name, r.lang)


# self parameter
# class Employee:
#     salary=100000 #class attributes
#     lang="py"

#     def getinfo(self):
#         print(f"language is {self.lang}")

#     @staticmethod
#     def greet():
#         print("good morning")
        

# t= Employee()
# t.lang="JS"
# print( t.salary, t.lang)
# t.getinfo()
# t.greet()

# __init__
# class Employee:
#     salary=100000 #class attributes
#     lang="py"

#     def __init__(self,name,salary,lang): #dunder method is automatically called 
#         self.name=name
#         self.salary=salary
#         self.lang=lang

#         print(f"i am creating a dunder")

#     def getinfo(self):
#         print(f"language is {self.lang} sal is {self.salary}")

#     @staticmethod
#     def greet():
#         print("good morning")
        

# t= Employee("harry",122222, "rust")
# # t.lang="JS"
# # t.name="tam"
# print( t.name, t.salary, t.lang)
# t.getinfo()
# t.greet()

#PRACTICE SET
#1
# class Programmer:
#     company="microsoft"
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

# obj1=Programmer("shubh",23000)

# obj2=Programmer("lmaop",23111)

# print(obj1.name,obj1.salary)
# print(obj2.name,obj2.salary,obj2.company)

#2 square cube and sq root
# import math
# class Calculator:
#     def calculate(self,n):
#         print("square is : ",n*n)
#         print("cube is : ",n*n*n)
#         print("square root is : ",math.sqrt(n))

# obj1=Calculator()
# n=int(input("enter number to calculate: "))
# obj1.calculate(n)

# #3
# class A:
#     a="smtg"

# object=A()
# object.a=0
# print(object.a) #instance attribute takes priority over class attribute

#4
# import math
# class Calculator:
#     def calculate(self,n):
#         print("square is : ",n*n)
#         print("cube is : ",n*n*n)
#         print("square root is : ",math.sqrt(n))

#     @staticmethod
#     def greet():
#         print("hello")

# obj1=Calculator()
# obj1.greet()
# n=int(input("enter number to calculate: "))
# obj1.calculate(n)

#5
# import random
# class Train:

#     rail="indian railways"

#     def __init__(self,tno):
#          self.tno=tno
    
#     def book(self,fro,to):
#         print(f"ticket is booked in train no : {self.tno} from {fro} to {to}")

#     def status(self):
#         print(f"train no {self.tno} is running on time")

#     def fare(self,fro,to):
#         print(f"fare in train no {self.tno} is {random.randint(222,444)} from {fro} to {to} ")


# p1=Train(12620)


# while True:
#     print("1. BOOK \n 2. GET STATUS \n 3. FARE_INFO\n4. EXIT \n")
#     ch=int(input("enter ur choice : "))

#     if ch == 1:
#         p1.book("mbai","mlore")
#     elif ch==2:
#         p1.status()
        
#     elif ch==3:
#         p1.fare("mbai","mlore") 
#     else:
#         break    

#6
# class Name:
#     def __init__(harry,name):
#         harry.name=name
# obj1=Name("reAL")
# print(obj1.name)



