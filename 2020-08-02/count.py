def list_count_4(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1

    return count

print(list_count_4([1, 6, 7, 4]))
print(list_count_4([1, 4, 6, 7, 4]))
print(list_count_4([1, 4, 6, 4, 7, 4]))
print(list_count_4([0, 4, 1, 6, 8, 4, 8, 4, 6, 7, 4, 6]))
print(list_count_4([4, 7, 4, 1, 6, 4, 9, 4, 6, 7, 5, 4]))
print(list_count_4([5, 4, 1, 2, 4, 6, 3, 4, 9, 5, 4, 6, 7, 4, 7, 3, 4, 9, 0]))
