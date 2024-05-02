def do_addition(a:int,b:int):
    return a + b
def do_sub(a:int,b:int):
    return a - b
def do_division(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        return "Cannot divide by zero"