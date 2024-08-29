import random

computer=random.choice([-1,0,1])
youStr=input("Enter your choice: ")
youDict={"s":1,"w":0,"g":-1}
revDict={1:"snake",0:"water",-1:"gun"}

you=youDict[youStr]

print(f"You chose {revDict[you]}\nComputer chose {revDict[computer]}")

if(computer==you):
    print("It's a draw")

else:
    if(computer==-1 and you==0):
        print("You win")

    elif(computer==-1 and you==1):
        print("Computer win")

    elif(computer==0 and you==-1):
        print("Computer win")

    elif(computer==0 and you==1):
        print("You win")

    elif(computer==1 and you==0):
        print("Computer win")

    elif(computer==1 and you==-1):
        print("You win")

    else:
        print("Something went wrong")