mycode = 'print("hello world")'
code = """
def mutiply(x,y):
    return x*y

print('Multiply of 7 and 9 is: ',mutiply(7,9))
"""
exec(mycode)
exec(code)