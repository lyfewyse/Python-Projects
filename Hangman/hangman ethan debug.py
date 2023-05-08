import random

# Initialize Difficulty
while True:
    difficulty_selection = input(
        'Select Difficulty : [1]Easy [2]Adept [3]Hard')

    # Initialize Word Bank per Difficulty
    words_easy = ['apple', 'monkey', 'phone', 'date']
    words_adept = ['demand', 'capital', 'captain', 'housing']
    words_hard = ['elderberry', 'capitalization', 'liquidity', 'absolution']

    # Initialize Word based on difficulty word bank
    if difficulty_selection == '1':
        words = random.choice(words_easy)
    elif difficulty_selection == '2':
        words = random.choice(words_adept)
    elif difficulty_selection == '3':
        words = random.choice(words_hard)
    else:
        print('Invalid input! Please enter 1, 2, or 3.')
        continue

    # Initialize lives
    if difficulty_selection == '1':
        health = 10
    if difficulty_selection == '2':
        health = 8
    if difficulty_selection == '3':
        health = 5

    # intiliaze guessed letters variable
    guessed_letters = []

    # Game Loop
    word = words
    lives = health
    while True:
        print('Good Luck')
        print(f"The word is {len(word)} letters long.")
        print(f"You have {lives} lives left.")
        print("Guessed Letters: ", guessed_letters)

        # display the current state of the word
        display = ''
        for letter in word:
            if letter in guessed_letters:
                display += letter
            else:
                display += '_'
        print(display)

        # Users guesses a letter, converts to lower case
        guess = input('Guess a letter: ').lower()

        # Check if guess is valid
        if len(guess) != 1 or not guess.isalpha():
            print('Invalid guess! Enter a single character!')

        if guess in guessed_letters:
            print('Invalid guess! You have already guessed this letter!')

        # add the guess to the guessed letters array
        guessed_letters.append(guess)

        # check if the guess is correct
        if guess in word:
            print('Correct!')
        else:
            print('Incorrect!')
            lives -= 1

        # check if game is over
        if lives == 0:
            print(f'Game Over! The word was {word}')
            break
        elif set(word) == set(guessed_letters):
            print(f'Congrats! You guessed the word! | {word}')
            break
