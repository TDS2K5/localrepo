#fibonacci series starts from 0,1

n=int(input("enter a number: "))
a=0
b=1
print(a,b)

for i in range(n):
    c=a+b
    a=b
    b=c
    print(c)