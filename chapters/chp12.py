#Advanced Python

#walrus operator
# if n:=len([1,2,3,4,5]) >=5:
#     print("walrus operator allows us to assign an expression to a variable")

#Type definitions 
# n : int = 5 
# # s: str = "lol" '''explicitly stating type'''
# def num(a:int, b:int) ->int : #stating argument type and return value type
#     return a + b

# print(num(4,5))


#typing module
# from typing import List,Union,Tuple,Dict

# l : List[int] = [1,2,3]
# print (l)

# t: Tuple[int,str] = (1,2,'a',3) #specified tuple has both int and str types
# print(t)


# match case
# def http_status(status):
#     match status:
#         case 200:
#          return "OK"
#         case 404:
#          return "Not Found"
#         case 500:
#           return "Internal Server Error"
#         case __:
#           return "Unknown status"
      
# print(http_status(200))
# print(http_status(404))
# print(http_status(500))
# print(http_status(0))

# '''OK
# Not Found
# Internal Server Error
# Unknown status'''


# Merge and update operators
# dict1={'a':1, 'b' : 2 }
# dict2= {'c':3, 'd':4}
# n= dict1 | dict2
# print(n)

# list comprehension and enumerate
# l=[1,2,3,4,5]
# n=[i for i in l] #list comprehension
# print(n)

# for i,item in enumerate(l): #enumerate function
#     print(f"index {i} contains item {item}")

# PRACTICE SET
# 1
# try:
#     with open ("1.txt") as f:
#         f.read()
# except Exception as e:
#     print(e)
# try:
#     with open ("2.txt") as f:
#         f.read()
# except Exception as e:
#     print(e)
# try:
#     with open ("3.txt") as f:
#         f.read()
# except Exception as e:
#     print(e)

# print("anyways")

#3
# n=int(input("enter a number: "))
# l=[i*n for i in range(11)]
# print(l)

#4
# try:
#     a=int(input("enter a : "))
#     b=int(input("enter b : "))
#     c=a/b
#     print(c)
# except ZeroDivisionError :
#     print('infinite')
# finally:
#     print('done')

#5
# n=int(input("enter a number: "))
# l=[i*n for i in range(11)]
# print(l)
# with open ("tables.txt","a") as f:
#     f.write(str(l))



