import random

# List of animals
animals = ['tiger', 'lion', 'giraffe', 'rhino', 'zebra', 'dolphin', 'shark']

# Randomly select a word
word = random.choice(animals).lower()

# Lists to track correct and incorrect guesses
guessed_correctly = []
guessed_incorrectly = []

# Number of tries
tries = 6

# Hangman count (not actually used in this version)
hangman_count = -1

# Main game loop
while tries > 0:
    output = ''
    # Construct the current state of the word
    for letter in word:
        if letter in guessed_correctly:
            output += letter
        else:
            output += '_ '
    
    # Check if the user has guessed the word
    if output.replace(' ', '') == word:
        break
    
    print("Guess the word:", output)
    print(tries, "chances left")

    # Get the user's guess (fixed the input() function call)
    guess = input().lower()

    # Check if the guess was already made
    if guess in guessed_correctly or guess in guessed_incorrectly:
        print("Already Guessed:", guess)
    elif guess in word:
        print("Awesome Job! You guessed a correct letter!")
        guessed_correctly.append(guess)
    else:
        print("Sorry! You guessed a wrong letter!")
        hangman_count += 1
        tries -= 1
        guessed_incorrectly.append(guess)

# Check if the user won or lost
if tries > 0:
    print("You guessed the word and you win!")
else:
    print("Sorry, you ran out of tries. The word was:", word)
