def rectangle(a, b):
    result = ''

    if not isinstance(a, int) or not isinstance(b, int):
        return "Enter valid values!"
    perimeter = 2*(a + b)
    area = a * b
    nl = "\n"
    result = f"Rectangle area: {area} {nl}Rectangle perimeter: {perimeter}"
    return result
    
print(rectangle(2, 10))

# def rectangle(length, width):
#     if not isinstance(length, int) or not isinstance(width, int):
#         return "Enter valid values!"

#     def area():
#         return length * width

#     def perimeter():
#         return 2*(length + width)

#     return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"

# print(rectangle(2, 10))
# print(rectangle('2', 10))