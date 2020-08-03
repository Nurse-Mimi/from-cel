def substring_copy(str, n):
    flen = 2
    if flen > len(str):
        flen = len(str)
    substr = str[:flen]


    result = ""
    for i in range(n):
        result = result + substr
    return result
print(substring_copy('abcdef', 2))
print(substring_copy('p', 3))
print(substring_copy('del', 9))
print(substring_copy('M', 56))
