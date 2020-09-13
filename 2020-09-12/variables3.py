
def func1():
    global var1
    var1 = "PHP"
    print("In side func1() var1 = ",var1)

def func2():
    print("In side func2() var1 = ",var1)
func1()
func2()
