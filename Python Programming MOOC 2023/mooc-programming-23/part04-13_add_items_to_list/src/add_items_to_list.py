# Write your solution here

list = []

items = int(input("How many items: "))
count = 0

while count < items:
    item = int(input(f"Item {count + 1}: "))
    list.append(item)
    count += 1

print(list)