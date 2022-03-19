from random import randint
from game_data import data
from art import logo, vs

listLenght= len(data)-1
randomeNumberA=randint(0,listLenght)
randomeNumberB= randomeNumberA - 1 # Thik of way to remove 1 list iteam each turn and make sure that numberA is never the same as numberB
counter = 0
game = True


def compare():
    print(logo)

    print(f"Compare A: {data[randomeNumberA]['name']}, {data[randomeNumberA]['description']}, from {data[randomeNumberA]['country']} HINT {data[randomeNumberA]['follower_count']}")
    print(f"Correct gueses {counter}")
    print(vs)

    print(f"Compare B: {data[randomeNumberB]['name']}, {data[randomeNumberB]['description']}, from {data[randomeNumberB]['country']} HINT {data[randomeNumberB]['follower_count']}")
    print("Who has more followers?")



    
while game:
    compare()
    answer = input("Your answer: ")

    if answer == "A":
        if data[randomeNumberA]['follower_count']>data[randomeNumberB]['follower_count']:
            print(f"{data[randomeNumberA]['name']} has more followers then {data[randomeNumberB]['name']}. You win")
            counter = counter +1
        elif data[randomeNumberA]['follower_count']<data[randomeNumberB]['follower_count']:
            print(f"{data[randomeNumberA]['name']} has more followers then {data[randomeNumberB]['name']}. You loose")
            game = False

    elif answer == "B":
        if data[randomeNumberB]['follower_count']>data[randomeNumberA]['follower_count']:
            print(f"{data[randomeNumberB]['name']} has more followers then {data[randomeNumberA]['name']}. You win")
            counter = counter +1
        elif data[randomeNumberB]['follower_count']<data[randomeNumberA]['follower_count']:
            print(f"{data[randomeNumberB]['name']} has more followers then {data[randomeNumberA]['name']}. You loose")
            game = False

   