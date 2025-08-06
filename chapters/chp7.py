# for with else
# l=[1,2,3]
# for i in l:
#     print(i)
# else:
#     print("done")

# for i in range (5):
#     if (i==2):
#         continue
#     print(i)
    



### practice set chap 7
# n=int(input("enter a number: "))
# for i in range(11):
#     p=n*i
#     print(f"{n} * {i} = {p}")

# n=int(input("enter a number: "))
# p=n*11
# for i in range(0,p,n):
#     print(i)


# l = ["Harry", "Soham", "Sachin", "Rahul"]
# for item in l:
#     if item.startswith('S'):
#         print(f"hello {item}")


# while loop multi
# n=int(input("enter a number: "))
# i=0
# while i<11:
#     print(f"{n} * {i} = {n*i}")
#     i+=1

 # prime nos
# n=int(input("enter a number: "))
# for i in range(2,n):
#     if n%i==0:
#         print("composite")
#         break
# else:
#     print('prime')

# n=int(input("enter : "))
# i=0
# l=[]
# while i<=n:
#     l.append(i)
#     i+=1
# d=sum(l)
# print(d,l)

# factorial using for loop
# n=int(input("enter a number: "))
# i=1
# fact=1
# for i in range(n):
#     fact+=fact*i
#     print(fact)
#     i+=1
# print(f"factorial is {fact}")


# # star pattern 1 3 5
# n=int(input("enter a number: "))
# for i in range (n):
#     print(" "*(n-i),end="")
#     print("*" *(2*i+1),end="")
#     print("")

# star pattern 1 2 3
# n=3
# for i in range(n+1):
#     st="*"
#     print(st*i)

#star pattern 3 101 3
# n=int(input("enter a number: "))
# for i in range(1,n+1):
#     if i==1 or i==n:
#         print("*"* n,end="")
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print('')


# multiplication table of n using for loop in reverse order
# n=int(input("enter a number: "))
# l=[]
# for i in range(11):
#     p=n*i
#     l.append(p)
# print(list(reversed(l)))

        
# n=int(input("enter a number : "))
# for i in range(11):
#     print(f"{n}*{11-i}={n*(11-i)}")
    




