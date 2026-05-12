import random

def get_a_number():
    while True:
        num = input("Enter a number guesses that you want to play: ")
        if chacks_number(num):
            return int(num)


def chacks_number(num):
    try:
        return int(num)
    except:
        print("Please enter a valid number...")


def hide_word(len):
    return "#" * len


def get_a_letter():
    while True:
        char = input("Please guess one letter: ")
        if checks_alpha(char):
            return char
        else:
            print("You must enter ONE valid letter...")


def checks_alpha(letter):
    return letter.isalpha() and letter.isascii() and (len(letter) == 1)


def show_status(inputed_letters, hidden_word, guess_times):
    print(f"""\n
      ---- HERE IS YOUR STATUS FOR NOW ----
    You already used this letters {inputed_letters}.
          The hidden eord is: {hidden_word}.
         Left you {guess_times} times to try.
      ------------- GOOD LUCK -------------\n
""")


def main():
    guesses_times = get_a_number()

    word_list = ["Bread", "Light", "Frame", "Storm", "Grape", "Cloud", "Point", "Match", "Brick", "Voice"]

    current_word = word_list[random.randint(0, len(word_list)-1)]
    print(current_word)

    hidden_word = hide_word(len(current_word))

    inputed_letters = []

    while guesses_times > 0:
        show_status(inputed_letters, hidden_word, guesses_times)

        users_guess = get_a_letter()

        if users_guess in current_word:
            for i, v in enumerate(current_word):
                if v == users_guess:
                    tmp_word = list(hidden_word)
                    tmp_word[i] = v
                    hidden_word = "".join(tmp_word)
                    break
            if hidden_word == current_word:
                break
        else:
            print("Don't give up!\nLet's try again...")
            guesses_times -= 1
        


    if guesses_times > 0:
        pass



if __name__ == "__main__":
    main()