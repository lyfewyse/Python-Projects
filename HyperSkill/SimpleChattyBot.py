import math
    #TO-DEV: LINE 21 Remainder is now calculated based on outcome of division
    #TO-DEV: LINE 24 float used to allow for decimal numbers now that Division outcome is the input value
    #TO-DEV: LINE 34 CIEL is used to round up the result
    #TO-DEV: LINE 93 function calls have been moved at the end of their sequential function rather than at the end of 
                    #initialization. Once greet() function is called, loop will occur until end

def greet(bot_name, birth_year):
    #Return Greeting
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')
    #Begin function call loop
    remind_name()


def remind_name():
    #Initialize Values for Name 
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')
    #Continue Function Call loop
    guess_age()


def guess_age():
    print('Let me guess your age.')
    #Intialize Values for Age
    rem3 = float(input('What is your age divided by 3!(Round to the nearest 3 decimal points)'))
    rem3_answer = rem3 * 3
    rem3_remainder = rem3_answer % 3
    rem5 = float(input('What is your age divided by 5!(Round to the nearest 3 decimal points)'))
    rem5_answer = rem5 * 5
    rem5_remainder = rem5_answer % 5

    rem7 = float(input('What is your age divided by 7!(Round to the nearest 3 decimal points)'))
    rem7_answer = rem7 * 7
    rem7_remainder = rem7_answer % 7
    age = math.ceil((rem3_remainder * 70 + rem5_remainder * 21 + rem7_remainder * 15) % 105)

    print("Your age is " + str(age) +
          "; that's a good time to start programming!")
    #Continue Function Call loop
    count()


def count():
    print('Now I will prove to you that I can count to any number you want.')

    #Intitialize counting variable
    user = int(input())
    number = 0
    while number <= user:
        print(number, '')
        number += 1
    #Continue Function Call loop
    question_1()


def question_1():
    print("Let's test your programming knowledge.")
    questions = ["What are functions used for?", "1. To repeat a statement multiple times.", "2. To decompose a program into several small subroutines.",
                 "3. To determine the execution time of a program.", "4. To interrupt the execution of a program."]
    # prints all [questions] instead of manually writing each print funciton
    for n in questions:
        print(n)
    # user input
    answer = int(input())
    # loop
    while answer != 2:
        print("Please, try again.")
        answer = int(input())
    if answer == 2:
        print('Good Job! Onto Question 2!')
    #Continue Function Call loop
    question_2()

def question_2():
    questions = ["What can a Boolean be equal to?", "1. Letter and Numbers.", "2. Only numbers.",
                 "3. True or False.", "4. Only Letters."]
    # prints all [questions] instead of manually writing each print funciton
    for n in questions:
        print(n)
    # user input
    answer = int(input())
    # loop
    while answer != 3:
        print("Please, try again.")
        answer = int(input())
    if answer == 3:
        print('Completed, have a nice day!')
    #Continue Function Call loop
    end()


def end():
    play_again = input('Would you like to play again![Y/N]').lower()
    if play_again == 'y':
        greet()
    else:
        print('Congratulations, have a nice day!')


# Call Greeting to begin loop
greet('Alva', '2023')  # change it as you need
