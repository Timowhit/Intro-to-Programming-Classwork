#This is Word Game 
#Author:Timothy Whitehead
import random #randomizer import

words = ["apple", "guess", "squid", "space"] #word list
random_word = random.choice(words) #picks random word from list
secret = random_word

guess = ''
hint = ''
guess_count = 0

for a in secret:
    hint = hint + '_ '

print("Welcome to the Word Guessing Game!")

while guess != secret:

    word_length = False

    while(not word_length):
        guess = input("What is your guess? ").lower()
        guess_count += 1

        if len(guess) != len(secret):
            print("The guess must have the same number of letters as the answer.")
        else:
            word_length = True

    if guess == secret:
        break

    hint = ''

    for i, a in enumerate(guess):

        for j, b in enumerate(secret):

            if(a == b and i == j):
                letter = a.capitalize() + ' '
            elif (a== b):
                letter = a + ' '
            elif (a != b):
                letter = '_ '

        hint = hint + letter

    print(f"Your hint is {hint}")


print(f"You have guessed correctly after {guess_count} tries.")