globVar = 10

print(globVar)


def fun():
    globVar = 5
    print(globVar)
    locVab = 20
    print(locVab)


fun()

# since globVar manipulated inside function, so outside the manupulation is not valid
print(globVar)
try:
    print(locVab)
except:
    print("unfound error occured because locVab was limited within fun() fn. only")


def fun2():
    locVab = 0
    global globVar  # it helps to manipulate the value of globVar globally inside any fn. but not recommended
    globVar = 5
    locVab = 20
    print(globVar)
    print(locVab)


fun2()

print(globVar)  # since globVar manipulated inside function using global keyword, so outside also the manupulation is valid
try:
    print(locVab)
except:
    print("unfound error occured because locVab was limited within fun() fn. only")
