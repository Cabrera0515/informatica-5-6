def main():

    print("Welcome to the times table quizz")
    #this values are for using them in the while loop
    not_validated = True
    while not_validated2 = True

    #we start the while loop for the question 1
        while not_validated:
        try:
            number = int(input("Enter a number between 1 and 10: "))
            if number >= 1 and number <= 10:
            print("Number stored successfully.")
            not_validated = False # -> break
        except ValueError:
            print("Enter a whole number!")

      while not_validated2:
        try:
            max_value = int(input("Enter the maximum value for your times table: "))
            if 1<= max_value <=10:
                not_validated2 = false
        except ValueError:
            print("Enter a whole number:")


        print(f"Here is your quizz on the (times_table) times table")

        for x in range(1, (max value + 1)):
        not_validated3 = True
        answer = x * times_table
        print(f"(x) times (times_table) is: ")
        while not_validated3:
            try:
            user_answer = int(input("The answer is? "))

    # while True:
    #




if __name__ == "__main__":
    main()

