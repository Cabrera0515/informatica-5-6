def main():
    not_validated = True
    while not_validated:
        try:
            number = int(input("Enter a number between 1 and 10: "))
            
            print("Number stored successfully.")
            not_validated = False # -> break
        except ValueError:
            print("Enter an integer NUMBER.")




if __name__ == "__main__":
    main()

