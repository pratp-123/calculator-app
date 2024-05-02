from calc_func import do_addition,do_sub,do_division
from multiply import do_multiplication
def main():
    print("Welcome to the calculator app")
    print("""\nSelect the function from given option
          1. Add 
          2. Substract
          3.multiply
          4.division
          """)

    user_input = input("Select the function")
    a = int(input("Enter first number"))
    b = int(input("Enter first number"))

    if user_input == "1":
        result = do_addition(a,b)
    elif user_input == "2":
        result = do_sub(a,b)
    elif user_input == "3":
        result = do_multiplication(a,b)
    elif user_input == "4":
        result = do_division(a,b)
    print("result",result)


if __name__ == "__main__":
    main()