# Write your solution here

def same_chars(string, integer1, integer2):
    if integer1 < 0 or integer1 >= len(string) or integer2 < 0 or integer2 >= len(string):
        return False
    
    integer1 = string[integer1]
    integer2 = string[integer2]
    if integer1 == integer2:
        return True
    else:
        return False
    

        

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 10))