# # prime nos
# n=int(input("enter a number : "))
# for i in range (2,n):
#     if n%i==0:
#         print("not a prime")
#         break
# else:
#     print("prime")

#sum of n natural nos
# n=int(input("enter a number : "))
# i=1
# sum=0
# while i<=n:
#     sum+=i
#     i+=1
# print("sum is : ",sum)

#factorial using for loop 
# n=int(input("enter a number : "))
# fact=1
# i=1
# for i in range(n):
#     fact+=fact*i
# print(fact)

#star pattern odd pyramid '''
'''
  *
 ***
*****
'''
# n=int(input("enter a number : "))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*(2*i-1),end="")
#     print("")

# star pattern normal 
# n=int(input("enter a number : "))
# for i in range(n+1):
#     print("*"*i)

#star ring pattern
# n=int(input("enter a number : "))
# for i in range(1,n+1):
#     if i==1 or i==n:
#         print('*'*n,end="")
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print("")
       
    # reverse multiplication table

# n=int(input("enter a number : "))
# for i in range(11):
#     print(f"{n} * {11-i} = {n*(11-i)}")


