# Write your solution here

def line(length, char):
    if not char:
        char = "*"
        print(length * char)
    else:
        char = char[0]
        print(length * char)
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(6, "-----")