def main():
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (add, substract, multiply, division): ")

    if operation == "add":
        result = num1 + num2
        print(result)
    elif operation == "substract":
        result = num1 - num2
        print(result)
    elif operation == "multiply":
        result = num1 * num2
        print(result)
    elif operation == "division":
         result = num1 / num2
         print(result)
    else:
         print("Invalid operation")


if __name__ == "__main__":
        main()
