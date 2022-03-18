from random import randint
from game_data import data
from art import logo, vs

randomeNumberA=randint(0,49)
randomeNumberB= randomeNumberA - 1

print(logo)

print(f"Compare A: {data[randomeNumberA]['name']}, {data[randomeNumberA]['description']}, from {data[randomeNumberA]['country']} ")

print(vs)

print(f"Compare A: {data[randomeNumberB]['name']}, {data[randomeNumberB]['description']}, from {data[randomeNumberB]['country']} ")

