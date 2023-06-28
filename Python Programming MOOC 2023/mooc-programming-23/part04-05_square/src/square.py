# Copy here code of line function from previous exercise
def line(length, char):
    if not char:
        char = "*"
        print(length * char)
    else:
        char = char[0]
        print(length * char)

def square(size, character):
    count = size
    while count > 0:
        line(size, character)
        count -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")