import random
word_bank = ['apple', 'banana', 'cherry']


chosen_word = random.choice(word_bank)

lives = 6
correct_guesses = []

while lives > 0:
    # Display the current state of the game
    print(f"Lives remaining: {lives}")
    print(
        f"Word: {'' .join([char if char in correct_guesses else '_' for char in chosen_word])}")

    # Ask the user for a guess
    guess = input("Guess a letter: ")

    # Check if the guess is correct
    if guess in chosen_word:
        print("Coorect!")
        correct_guesses.append(guess)
    else:
        print("Incorrect.")
        lives -= 1

    # Check if the game is over
    if set(correct_guesses) == set(chosen_word):
        print("Congratulations, you win!")
        break

if lives == 0:
    print(f"Sorry, you lose. The word ws {chosen_word}.")
