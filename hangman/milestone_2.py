import random

word_list = ["apple", "banana", "orange", "grape", "kiwi"]
word = random.choice(word_list)
guess = input("Enter a single letter: ")

print(word_list)
print("Randomly chosen word:", word)

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

