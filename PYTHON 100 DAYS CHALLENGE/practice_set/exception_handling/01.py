def fun():
    try:
        num1 = int(input("Enter 1st number : "))
        num2 = int(input("Enter 2nd number : "))
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    except ZeroDivisionError:
        print("kripya 0 se bhag na de")
    except ValueError:
        print("please enter an integer")
        fun()
    finally:
        print("don't come again")

fun()
