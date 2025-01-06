def even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."


result = even_or_odd(2)
print(result)
print(even_or_odd(15))
