def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number(6))
print(perfect_number(-9))
print(perfect_number(0))
print(perfect_number(-31))
print(perfect_number(9877653))
print(perfect_number(7))
print(perfect_number(-14))
