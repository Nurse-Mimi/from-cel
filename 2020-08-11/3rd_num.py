def delete_num(int_list):
    spot = 3 - 1
    idx = 0
    list_len = (len(int_list))
    while list_len > 0:
        idx = (spot + idx) % list_len
        print(int_list.pop(idx))
        list_len -= 1

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
delete_num(numbers)
