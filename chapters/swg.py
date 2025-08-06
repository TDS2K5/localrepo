'''
1 = snake
2 = water
3 = gun
'''



import random

cpu=random.choice([1,2,3])

# user input choice 
youin=input("enter ur choice : s,w,g: ")

# store user choice in dictionary as number
youdict={'s':1, 'w' : 2, 'g' : 3}

# if user input key is available in dict, store corresponding value in another variable 'you'
you=youdict[youin]

# dictionary to convert computer number to string for printing
revDict={1:"snake", 2:"water", 3:"gun"}

# else if ladder
if cpu == you :
    print("tied")

else:
    if you == 1 and cpu == 2:
        print(f"you chose : {revDict[you]}\n cpu chose : {revDict[cpu]}\n you won ")
    elif you == 1 and cpu == 3:
        print(f"you chose : {revDict[you]}\n cpu chose : {revDict[cpu]}\n you lose ")
    elif you == 2 and cpu == 1:
        print(f"you chose : {revDict[you]}\n cpu chose : {revDict[cpu]}\n you lose ")
    elif you == 2 and cpu == 3:
        print(f"you chose : {revDict[you]}\n cpu chose : {revDict[cpu]}\n you won ")
    elif you == 3 and cpu == 1:
        print(f"you chose : {revDict[you]}\n cpu chose : {revDict[cpu]}\n you won ")
    elif you == 3 and cpu == 2:
        print(f"you chose : {revDict[you]}\n cpu chose : {revDict[cpu]}\n you lose ")
    
    else: print("error")

# optional logic 
# else:
#     if (you-cpu) == -1 or (you-cpu) == 2:
#         print(f"you chose : {revDict[you]}\n cpu chose : {revDict[cpu]}\n you won ")
#     else :
#         print(f"you chose : {revDict[you]}\n cpu chose : {revDict[cpu]}\n you lose ")