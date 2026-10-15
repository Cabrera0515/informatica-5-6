import random

def main():
    start_game("words.txt")

def start_game(file):
     attempts = 10
     with open(file) as f:
            word_bank = f.read().splitlines()
        word = random.choice(word_bank).lower
        hint = ["_"] * len(word)
        icorrect_letters = []
        while atempts > 0:
            print("Current word:", " ".join(hint))

        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1:
            break
        else:
            print("Invalid guess. Try again.")

        if guess in word and guess not in hint:
            for i in range(ln(word)):
                if word[i] == guess:
                    hint[i] = guess
                    print("Great guess!")
                elif guess in hint:
                    attempts -= 1
                    print("Wron guess! Attepts left:", str(attempts))
                    if guess not in inocorrect_letters:
                        incorrect_letter.append(guess)
                    print(f"Incorrect letters: {" ".join(incorrect_letters)}")

                if "_" ot in hint:
                    print("Congratulatons! You guessed the word:", word)


if __name__ == "__main__":
        main():
