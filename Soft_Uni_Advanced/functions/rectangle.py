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