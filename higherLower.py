from random import randint
from game_data import data
from art import logo, vs
import os


listLenght= len(data)-1
randomeNumberA=randint(0,listLenght)
#data.remove()
randomeNumberB= randint(0,listLenght) 

def genNewNumberB(randomeNumberA, randomeNumberB):
   
    while randomeNumberA == randomeNumberB:
        if randomeNumberA == randomeNumberB:
            randomeNumberB= randint(0,listLenght)
            
            return randomeNumberB
        else:
            pass
       

def compare():
    print(logo)

    print(f"Compare A: {data[randomeNumberA]['name']}, {data[randomeNumberA]['description']}, from {data[randomeNumberA]['country']} HINT {data[randomeNumberA]['follower_count']}")
    print(f"Correct gueses {counter}")
    print(vs)

    print(f"Compare B: {data[randomeNumberB]['name']}, {data[randomeNumberB]['description']}, from {data[randomeNumberB]['country']} HINT {data[randomeNumberB]['follower_count']}")
    print("Who has more followers?")



print(type(genNewNumberB(randomeNumberA, randomeNumberB)))

counter = 0
game = True
clear = lambda: os.system('cls')

    
while game:
    compare()
    answer = input("Your answer: ")

    if answer == "A":
        if data[randomeNumberA]['follower_count']>data[randomeNumberB]['follower_count']:
            print(f"{data[randomeNumberA]['name']} has more followers then {data[randomeNumberB]['name']}. You win")
            counter = counter +1
            randomeNumberB= randint(0,listLenght) 
            clear() 
        elif data[randomeNumberA]['follower_count']<data[randomeNumberB]['follower_count']:
            print(f"{data[randomeNumberA]['name']} has less followers then {data[randomeNumberB]['name']}. You loose")
            game = False

    elif answer == "B":
        if data[randomeNumberB]['follower_count']>data[randomeNumberA]['follower_count']:
            print(f"{data[randomeNumberB]['name']} has more followers then {data[randomeNumberA]['name']}. You win")
            counter = counter +1
            randomeNumberA=randomeNumberB
            randomeNumberB= randint(0,listLenght) 
            clear() 
        elif data[randomeNumberB]['follower_count']<data[randomeNumberA]['follower_count']:
            print(f"{data[randomeNumberB]['name']} has less followers then {data[randomeNumberA]['name']}. You loose")
            game = False

           

   