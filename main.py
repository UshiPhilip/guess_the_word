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
    pass


def checks_alpha(letter):
    pass


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

    hidden_word = hide_word(len(current_word))

    inputed_letters = []

    while guesses_times > 0:
        show_status(inputed_letters, hidden_word, guesses_times)

    if guesses_times > 0:
        pass



if __name__ == "__main__":
    main()