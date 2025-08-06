#1 
# with open ("poems.txt") as f :
#     readd=f.read()
#     if "twinkle" in readd:
#         print("exists")

# 2 game()
# import random
# def game():
#     print("playing game")
#     score= random.randint(1,100)

#     # read the file and take its highscore (in str) as integer
#     with open ("hiscore.txt") as h:
#         high=h.read()
#         if(high!=""):
#             high=int(high)
#         else:
#             high=0

#     print(f"score : {score}")
    
#     if score>high :
#         with open ("hiscore.txt","w") as h:
#             h.write(str(score))
#     return score
# game()


# 3 table
# def gentable(n):
#     table=""
#     for i in range(1,11):
#         table += f"{n} x {i} = {n*i}\n"

#     with open (f"tables/table_{n}.txt","w") as f: 
#         f.write(table)

# for i in range (2,21):
#     gentable(i)

# 4 donkey
# word="donkey"
# with open ("file.txt", "r") as f :
#     content=f.read()

# contentnew=content.replace("donkey","****")

# with open ("file.txt", "w") as f :
#     f.write(contentnew)

#5
# word=["donkey","fuck","nigga"]

# with open ("file.txt", "r") as f :
#     content=f.read()

# for w in word:
#   content=content.replace(w,"*"*len(w))

# with open ("file.txt", "w") as f :
#     f.write(content)

#6
# with open ("log.txt") as f:
#     content=f.read()

# if "python" in content:
#     print("yes")
# else:
#     print("no")

# 7

# with open ("log.txt") as f:
#     lines=f.readlines()
# lineno=1
# for line in lines:
#     if "python" in line:
#         print(f"yes, lineno : {lineno}")
#         break
#     lineno+=1
# else:
#     print("no")

#8
# with open("this.txt") as f:
#     content=f.read()
# with open("this_copy.txt","w") as f:
#     f.write(content)

# 9
# with open("this.txt") as f:
    #  content=f.read()
# with open("this_copy.txt") as f:
#     content2=f.read()
# if content==content2:
#      print("identical")
# else:
#      print("no not identical")

# 10
# with open("this_copy.txt","w") as f:
#      f.write("")

# 11
# with open("old.txt") as f:
#     content=f.read()

# with open("renamed-by-py.txt","w") as f:
#      f.write(content) 


