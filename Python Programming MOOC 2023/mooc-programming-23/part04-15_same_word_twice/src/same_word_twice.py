# Write your solution here

my_list = []
count = 1

while True:
    word = input("Word: ")
    if word in my_list:
        print(f"You typed in {count - 1} different words")
        break
    else:
        my_list.append(word)
    count += 1
    