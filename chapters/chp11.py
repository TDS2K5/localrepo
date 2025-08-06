#INHERITANCE AND OOPS
# class Employee:
#     def show(self):
#         print(f"name of the employee is {self.name} and salary is {self.salary}")

# e1=Employee()
# e1.name='w'
# e1.salary=12
# e1.show()

# class Employee:
#     def show(self):
#         print(f"name of the employee is {self.name} and salary is {self.salary}")

# class Coder:
#     lang="py"
#     def printlang(self):
#         print(f"ur language is {self.lang}")

# class Programmer(Employee,Coder):
#     def lan(self):
#         print(f"name of the programmer is {self.name} and language is {self.lang}")
# e1=Employee()
# e1.name='w'
# e1.salary=12
# e1.show()

# p1=Programmer()
# p1.name="f"
# p1.salary=2
# p1.show()

# p1.lan()

# class Employee():
#     def __init__(self):
#         print("constructor of Employee")
#     a=1

# class Coder(Employee):
#     def __init__(self):
#         super().__init__()
#         print("constructor of Coder")
#     b=2

# class Manager(Coder):
#     def __init__(self):
#         super().__init__()
#         print("constructor of Manager")
#     c=3

# o=Employee()
# print(o.a)

# o=Coder()
# print(o.a, o.b)

# o=Manager()
# print(o.a, o.b, o.c)

# class attributes
# class Sm:
#     def show(self):
#         a=2
#         print(f"value of a is {self.a}") #instance attributes

# o=Sm()
# o.a=12
# o.show()

# class Emp:
#     a=2
#     @classmethod
#     def show(self):
        
#         print(f"value of a is {self.a}") #class attributes

# o=Emp()
# o.a=12
# o.show()

# property decorators
# class Emp:
#     a=2
#     @classmethod
#     def show(self):
#         print(f"value of a is {self.a}") #class attributes

#     @property
#     def name(self):
#         return self.oname
    
#     @name.setter
#     def name(self,value):
#         self.oname=value

# o=Emp()
# o.a=12
# o.name="ta"
# print(o.name)
# o.show()


# operator overloading
# class Number:
#     def __init__(self,n):
#         self.n=n

#     def __add__(self,num): # dunder method for operation
#         return self.n + num.n
# n=Number(1)
# m=Number(2)
# print(n+m)

#PRACTICE SET
# 1
# class Twodv :
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j

#     def show(self):
#         print(f"the vector is {self.i}i + {self.j}j ")

# class Threedv(Twodv) :
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k
#     def show(self):
#         print(f"the vector is {self.i}i + {self.j}j + {self.k}k")

# o = Twodv(1,2)
# b=Threedv(1,2,3)
# o.show()
# b.show()

# 2
# class Animals :
#     def show(s):
#         print("some generic sound")

# class Pets(Animals):
#     def lol(s):
#         print("cute pet")

# class Dog(Pets):
#     def bark(s):
#         print("dog is barking")

# a=Animals()
# b=Pets()
# c=Dog()

# c.lol()

# 3
# class Employee :
#     def __init__(self,salary,increment):
#         self.salary=salary
#         self.increment=increment
        
#     def inc(self,salary,increment):
#         increment+= (salary*5)/100
#         print(f"increment is : {increment}")
#         print(f"salary is : {salary+increment}")

# e=Employee(15000,5)
# e.inc(15000,5)

# 4
# class Employee :
#     def __init__(self,salary,increment):
#         self.salary=salary
#         self.increment=increment
#     @property    
#     def inc(self):
#         self.increment+= (self.salary*5)/100
#         print(f"increment is : {self.increment}")
#         print(f"salary is : {self.salary+self.increment}")


# e=Employee(15000,5)
# e.inc

# class Complex:
#     def __init__(self,r,i):
#         self.r=r
#         self.i=i
#     def __add__(self,c2):
#         return Complex(self.r+c2.r, self.i+c2.i)
#     def __mul__(self,c2):
#         return Complex(self.r+c2.r, self.i+c2.i)
#     def __str__(self):
#         return f"{self.r} + {self.i}i"

# c=Complex(1,2)
# c2= Complex(3,4)
# print(c+c2)
