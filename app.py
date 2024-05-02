from calc_func import do_addition,do_sub
from area import calculate_area_rectangle
def main():
    print("Welcome to the calculator app")
    print("""\nSelect the function from given option
          1. Add 
          2. Substract
          3. area
          """)

    user_input = input("Select the function")
    a = int(input("Enter first number"))
    b = int(input("Enter first number"))

    if user_input == "1":
        result = do_addition(a,b)
    elif user_input == "2":
        result = do_sub(a,b)
    elif user_input == "2":
        result = calculate_area_rectangle(a,b)
    print("result",result)


if __name__ == "__main__":
    main()