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
    pass


def main():
    guesses_times = get_a_number()

    word_list = ["Bread", "Light", "Frame", "Storm", "Grape", "Cloud", "Point", "Match", "Brick", "Voice"]

    current_word = word_list[random.randint(0, len(word_list)-1)]

    hidden_word = hide_word(len(current_word))

    inputed_letters = []

    while guesses_times > 0:
        pass

    if guesses_times > 0:
        pass



if __name__ == "__main__":
    main()