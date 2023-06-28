# Copy here code of line function from previous exercise
def line(length, char):
    if not char:
        char = "*"
        print(length * char)
    else:
        char = char[0]
        print(length * char)

def square_of_hashes(size):
    count = size
    while count > 0:
        line(size, "#")
        count -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(3)
