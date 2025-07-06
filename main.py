#snake water gun
import random

# n=int(input("enter ur choice: "))

#computer move
def cpu(ch):
    r=random.randint(1,3)
    if r == 1:
        print("cpu chose : snake \n ")
        score(ch,r)
        return 
        
    
    elif r==2:
        print("cpu chose : water \n ")
        score(ch,r)
        return 
        

    elif r ==3 :
        print("cpu chose : gun \n ")
        score(ch,r)
        return 
    
    else :
        pass

def score(ch,r):
    sc=0
    cp=0

    #snake vs cpu
    if ch==1 and r == 1 :
        
        print(f"tied\n your score is : {sc}\n cpu score is : {cp} \n ")
        
    

    elif ch==1 and r==2:
        sc+=1
        print(f"u won \n your score is : {sc}\n cpu score is : {cp}\n ")
        
    
    elif ch==1 and r==3:
        cp+=1
        print(f"u lose \n your score is : {sc}\n cpu score is : {cp}\n")
        
    
    #water vs cpu
    elif ch==2 and r == 1 :
        cp+=1
        print(f"u lose \n your score is : {sc}\n cpu score is : {cp}\n ")
         

    elif ch==2 and r==2:
        
        print(f"tied \n your score is : {sc}\n cpu score is : {cp} \n ")
    
    
    elif ch==2 and r==3:
        sc+=1
        print(f"u won \n our score is : {sc}\n cpu score is : {cp}  \n")
    
    
    #gun vs cpu
    elif ch==3 and r == 1 :
        sc+=1
        print(f"u won \n your score is : {sc}\n cpu score is : {cp} \n  ")
    

    elif ch==3 and r==2:
        cp+=1
        print(f"u lose \n your score is : {sc}\n cpu score is : {cp}  \n")
    
    
    elif ch==3 and r==3:
        
        print(f"tied \n your score is : {sc}\n cpu score is : {cp} \n ")
    
    
    
    
def main():
    while True:
        print("SNAKE WATER GUN\n 1. Snake \n 2. Water\n 3. Gun\n 4. Exit")
        ch=int(input("enter ur choice: "))
        

        if ch==1:
            print("u chose: snake")
            
            cpu(ch)  
            

        elif ch==2:
            print("u chose: water")
            
            cpu(ch)
            

        elif ch==3:
            print("u chose: gun")
            
            cpu(ch)
            

        elif ch==4:
            print("exiting... ")
            break
        elif ValueError:
            print("invalid choice...")
            break
        




if __name__=="__main__":
    main()