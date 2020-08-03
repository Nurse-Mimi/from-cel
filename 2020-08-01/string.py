def new_string(str):
    if len(str) >= 2 and str [:2] == "ls":
        return str
    return "ls" + str

print(new_string("Array"))
print(new_string("lsEmpty"))
