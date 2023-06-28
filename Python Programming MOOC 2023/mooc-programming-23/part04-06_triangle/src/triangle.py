# Copy here code of line function from previous exercise
def line(length, char):
    if not char:
        char = "*"
        print(length * char)
    else:
        char = char[0]
        print(length * char)

def triangle(size):
    count = 1
    while count <= size:
        line(count, "#")
        count += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
