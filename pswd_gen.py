import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&amp;*1234567890"
length = int(input("Enter your password length: "))
password = ""

for i in range(length+1):
    password+=random.choice(characters)
print(password)