# Write your solution here

while True:
    editor = input("Editor: ")
    editor = editor.lower()
    if editor == "visual studio code":
        print("an excellent choice!")
        break
    elif editor == "word" or editor == "notepad":
        print("awful")
    else:
        print("not good")