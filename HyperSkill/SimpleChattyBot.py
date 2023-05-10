print('Hello! My name is Alva.')
print('I was created in 2023.')
print('Please, remind me your name.')

# reading a name
user_name = input()
print(f'What a great name you have, {user_name}!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

# reading all remainders
remainder3 = int(input("Remainder 3: "))
remainder5 = int(input("Remainder 5: "))
remainder7 = int(input("Remainder 7: "))

your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print(f"Your age is {your_age}; that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')

# read a number and count to it here
print('Enter a number:')
number = 0
user = int(input())
while number <= user:
    print(number, "!")
    number += 1
print('Completed, have a nice day!')
