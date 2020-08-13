def add(a, b):
    while b != 0:
        data = a & b
        a = a ^ b 
        b = data << 1
    return a

print(add(5, 7))
print(add(86, 22))
print(add(-47, 81))
print(add(-4, -65))
print(add(4, 9))
print(add(-9, 9))