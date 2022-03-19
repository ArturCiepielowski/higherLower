from random import randint
from game_data import data
from art import logo, vs

randomeNumberA=randint(0,49)
randomeNumberB= randomeNumberA - 1
counter = 0
game = True


def compare():
    print(logo)

    print(f"Compare A: {data[randomeNumberA]['name']}, {data[randomeNumberA]['description']}, from {data[randomeNumberA]['country']} ")

    print(vs)

    print(f"Compare A: {data[randomeNumberB]['name']}, {data[randomeNumberB]['description']}, from {data[randomeNumberB]['country']} ")
    print("Who has more followers?")

    

compare()
answer = input("Your answer: ")

if answer == "A":
    if data[randomeNumberA]['follower_count']>data[randomeNumberB]['follower_count']:
       print(f"{data[randomeNumberA]['name']} has more followers then {data[randomeNumberB]['follower_count']}. You win")
       counter = counter +1
    elif data[randomeNumberA]['follower_count']<data[randomeNumberB]['follower_count']:
        print(f"{data[randomeNumberA]['name']} has more followers then {data[randomeNumberB]['follower_count']}. You loose")

elif answer == "B":
    print(f"{data[randomeNumberB]['follower_count']}")  
   