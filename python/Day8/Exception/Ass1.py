try:
    a=int(input("Enter the num1"))
    b=int(input("Enter the num2"))
    res=a/b
    print(res)
except ValueError :
    print("you have Entered Wrong Input")
except ZeroDivisionError:
    print("Zero Div Error")
except Exception:
    print("Other Error")
    
    