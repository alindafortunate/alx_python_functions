count = 0  # Global variable.


def increment():
    count += 1  # This referers to the local count within the function.
    
    increment()


print(count)
