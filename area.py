def calculate_area(length, width):
    """calculates the area of the rectangle."""
    area = length * width
    return area


length = 5.6
width = 4.2
print(f"The area is {calculate_area(length, width)} cm.")
print(f"The area is {calculate_area(10,5)} cm")
print(f"Area is {calculate_area(width=20, length=40)}")
