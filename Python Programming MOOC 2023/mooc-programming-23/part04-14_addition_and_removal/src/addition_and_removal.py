# Write your solution here

list = []
print(f"The list is now {list}")
count = 0

while True:
    answer = input("a(d)d, (r)emove or e(x)it: ")
    if answer == "d":
        list.insert(count, count + 1)
        print(f"The list is now {list}")
        count += 1

    if answer == "r":
        list.pop(count - 1)
        print(f"The list is now {list}")
        count -= 1

    if answer == "x":
        print("Bye!")
        break