def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply((8, 2, 3, -1, 7)))
print(multiply((54, 6, 9, 76)))
print(multiply((33, -8, 9, 4, 123)))
print(multiply((2, 234, 89, 61)))
