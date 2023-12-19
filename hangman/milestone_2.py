import random

fruits = ["apple", "banana", "orange", "grape", "kiwi"]
random_word = random.choice(fruits)
guess = input("Enter a single letter: ")

print(fruits)
print("Randomly chosen word:", random_word)

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

