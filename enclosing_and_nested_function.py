def outer_function():
    x = 10  # Variable in the enclosing function.

    def inner_function():
        nonlocal x  # Using nonlocal modify the x in the enclosing function
        x += 1  # Modifying the value of X.

    inner_function()
    print(f"Modified value of x from inner function:{x}")


outer_function()
