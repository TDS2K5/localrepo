#  FUNCTIONS AND RECURSIONS

#function to greet good day
# def gd():
#     n=input("enter a name : ")
#     print(f" hello {n}")
# gd()

#  function with arguments
# def car(name,year):
#     print(f"this car is a {name},{year}")

# car("bmw",2020)
# car("rolls",1990)
# car("merc",2052)

#return statement
# def add(a,b):
#     return(a+b) #allows us to store the value
# c=add(4,3) #returns the value when its called
# print(c-1)
#print simply displays the value, while return allows us to store it

# def car(name,year=2020):
#     print(f"this car is a {name},{year}")

# car("bmw",2000)
# car("rolls")
# car("merc",2052)

#recursion 
# factorial problem

# ''' 5! = 5x4x3x2x1 => n!=n(n-1)x(n-2)....3x2x1 => n!=n(n-1)!   '''

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
    
# n=int(input("enter a number : "))
# print(fact(n))

# PRACTICE SET
#1
# def great(a,b,c):
#     return max(a,b,c)
# a=int(input("enter the nos : "))
# b=int(input("enter the nos : "))
# c=int(input("enter the nos : "))
# print(great(a,b,c))

#2
# def convert(c):
#     return 
# c=int(input("enter the celcius : "))
# print("f is ",convert(c))

#3
# print("old line ")
# print("middle line",end="")
# print("latest line")

#4
# ''' first n natural nos are given by
# 1+2+3=6
# 1+2+3+4=10
# sum(n)=n+sum(n-1)
# '''
# def sum(n):
#     if n==1:
#         return 1
#     else:
#         return n+sum(n-1)
# n=int(input("enter n : "))
# print(sum(n))

#5
# def star(n):
#     for i in range(1,n+1):
#         print('*'*(4-i))
# n= int(input("enter n : "))
# star(n)

# def star(n):
#     if n==0:
#         return
#     print('*'*n)
#     star(n-1)

# n= int(input("enter no : "))
# star(n)


#6 inches to cms
# def cv(i):
#     return i * 2.54
# i= int(input("enter inch : "))
# print(f"cm is : {cv(i)}")

# 7 remove from list and strip
# def rm(l,r):
#     li=[]

#     for i in l:
#         if i!=r:
#             li.append(i.strip(r))
#     return li
# l=[]
# n= int(input("enter number of words : "))
# for i in range(n):
#     w=(input("words: "))
#     l.append(w)
# r=input("enter word to remove : ")
# print(rm(l,r))


#table function
# def table(n):
#     for i in range(11):
#         print(f"{n*i}")
# n = int(input("enter n : ")) 
# print(f"{table(n)}")

