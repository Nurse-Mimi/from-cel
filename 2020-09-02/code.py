mycode = 'print("hello world")'
code = """
def mutiply(x,y):
    return x*y

print('Multiply of 9 and 56 is: ',mutiply(9,56))
"""
exec(mycode)
exec(code)