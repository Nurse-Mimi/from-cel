def difference(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False

print(difference([2, 3, 6, 8, 4, 0]))
print(difference([1, 7, 3, 9, 0, 5, 3, 6]))
print(difference([7, 5, 8, 1, 4, 6, 3, 5, 8, 4]))
