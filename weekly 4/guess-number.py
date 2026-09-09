import random

def main():
    Name = input("Hello! What is your name?")
    print("Well, {name}, I am thinking of a number between 1 and 100.")
    print("medium level")
    print("Easy 1- 10")
    print("Medium 1-1000")
    print("hard 1-100000")

    level = input("Choose a difficulty level: ").strip().lower()
    if level == ("Easy"):
        print("level selected", level)
        guess = random.randint(
            print("Well,-, name, "I am thinking of a number in between 1 and 10.")

     if level == ("medium"):
        print("You selected level", level)
        guess = random.randint(1, 1000)
        print("Well,-, name, "I am thinking of a number in between 1 and 1000.")

     if level == ("Hard"):
        print("You selected level!, level)
              guess = random.randint(1, 100000)



        )
    print("I am thinking of a number between 1 and 100.")
    print("Take a guess")
