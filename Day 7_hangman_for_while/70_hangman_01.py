import random

#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)

# ex) chosen_Word = camel

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

# ex) user_guess = a

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in list(chosen_word):
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

# Me

# for letter in list(chosen_word):
#     if guess in letter:
#         print("Right")
#     else:
#         print("Wrong")