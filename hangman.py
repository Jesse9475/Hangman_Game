

HANGMAN_PICS = [
    '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
      |
      |
      |
     ==='''
]

# prepare a dictionary
import nltk

import random

nltk.download('words')

from nltk.corpus import words

word_list = words.words()

print("Original vocabulary size: ", len(word_list))

# list comprehension
temp_list = [word for word in word_list if len(word)>=3 and len(word)<8]

print("Candidate vocabulary size: ", len(temp_list))

word_list = temp_list


target_word = random.choice(word_list)
correct_letters = ['_'] * len(target_word)
lettered_word = []

used_letters = []
incorrect_letters = []
lives = 6
for n1 in range(0, len(target_word)):
    lettered_word.append(target_word[n1])

while lives > 0:
    value = False
    print("If you want to quit, print 'quit'")
    letter_input = input('Pick a letter in the english alphabet:')
    if letter_input == 'quit':
        break
    used_letters.append(letter_input)
    for n2 in range(0, len(target_word)):
        if letter_input == lettered_word[n2]:
            correct_letters[n2] = letter_input
            value = True
    if value != True:
        lives -= 1
    #print(correct_letters)
    print(" ".join(correct_letters))
    print(HANGMAN_PICS[lives])
    if correct_letters == lettered_word:
        print('GAME OVER, YOU WON')
        break

if lives == 0:
    print("GAME OVER TRY AGAIN")
