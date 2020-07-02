hangman.py

import random

Name = input("Your first name")

print ("Good Luck!", name)

words = ['rainbow, science, programming, python, board, water, chicken']

word = random.choice(words)

print("guess the characters")

guesses = ''

turns = 10

while turns > 0:
False = 0

for char in word:

  if char in guesses:
    print(char)

    else:
      print("_")

      False += 1

if False == 0;

print("You Win")

print("The word is:", word)
break

guess = input("guess a character:")

guesses += guess

if guess not in word:
  
  Print("Wrong")

  print("you have", + turn, 'more guesses')

  if turns == 0;
    
    print("you loose")