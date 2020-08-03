n = int(input("key in first number: "))
n2 = int(input("key in second number: "))
if n2 <= n:
    print(n - n2)
else:
    print((n2 - n) * 2)
