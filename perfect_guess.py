import random
n=random.randint(1,50)
a=-1
guesses=0

while(a!=n):
    guesses+=1
    a=int(input("Guess the number: "))
    if(a>n):
        print("Enter lower no please")
    else:
        print("Enter higher no please")

print(f"You have guessed the no {n} in {guesses} attempt")