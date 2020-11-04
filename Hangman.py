"""
Hangman Game.
"""

#############
# CONSTANTS #
#############
HANGMAN_ASCII_ART = ("  _    _\n"
                     " | |  | |\n"
                     " | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __\n"
                     " |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \n"
                     " | |  | | (_| | | | | (_| | | | | | | (_| | | | |\n"
                     " |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|\n"
                     "                      __/ |\n"
                     "                     |___/        "
)
HANGMAN_PHOTOS = {1:
                      """
    x-------x
    """, 2:
                      """
    x-------x
    |
    |
    |
    |
    |
    """, 3:
                      """
    x-------x
    |       |
    |       0
    |
    |
    |
    """, 4:
                      """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """, 5:
                      """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """, 6:
                      """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """, 7:
                      """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """}
MAX_TRIES = 6
UNDERSCORE_STR = " _ "
NOT_UPDATED_STR = "X\n{0}"
WINNER_MSG = "WIN"
LOSER_MSG = "LOSE"
BAD_GUESS_STR = "):"


def print_intro():
    """
    Function to print intro.
    """
    print(HANGMAN_ASCII_ART + "\n" + str(MAX_TRIES))


def check_win(secret_word, old_letters_guessed):
    """
    Function to check if all letters of secret word are in the list of previous guesses
    :param secret_word: string of secret word
    :param old_letters_guessed: list of previous guesses
    :return: True if all letters of secret word are in the list of previous guesses and False if not
    """
    count = 0
    for letter in secret_word:
        if letter in old_letters_guessed:
            count += 1
            continue
    return count == len(secret_word)


def show_hidden_word(secret_word, old_letters_guessed):
    """
    Function to check the index of correct letters guessed from the secret word
    :param secret_word: string of secret word
    :param old_letters_guessed: list of previous guesses
    :return: new string shows the correct letters and its position
    """
    new_string = ""
    index = 0
    while index < len(secret_word):
        if secret_word[index] in old_letters_guessed:
            new_string += secret_word[index]
        else:
            new_string += UNDERSCORE_STR
        index += 1
    return new_string


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Function to check if input is valid
    :param letter_guessed: single letter currently guessed
    :param old_letters_guessed: list of all previous guesses
    :return: True for valid input and False for not
    """
    return len(letter_guessed) == 1 and letter_guessed.isalpha() \
        and not letter_guessed.lower() in old_letters_guessed


def update_letters_guessed(letter_guessed, old_letters_guessed):
    """
    Function to add letter to old letter lists
    only if the letter is valid. else, prints the old list.
    :param letter_guessed: single letter currently guessed
    :param old_letters_guessed: list of all previous guesses
    :return: True if added, False if not.
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print_list_not_updated(old_letters_guessed)
        return False


def print_list_not_updated(my_list):
    """
    Function to check if input is valid
    :param my_list: list of all previous guesses
    prints previous guesses in list, in the requested format of a -> b ->c
    """
    print(NOT_UPDATED_STR.format(" -> ".join(sorted(my_list))))


def hangman(secret_word):
    """
    Game function.
    """
    num_of_tries = 1
    good_guess = False
    old_letters_guessed = []
    print_intro()
    print(HANGMAN_PHOTOS[num_of_tries])
    print(show_hidden_word(secret_word, old_letters_guessed))
    while num_of_tries <= MAX_TRIES:
        while not good_guess:
            letter_guessed = input("Guess a letter: ")
            good_guess = update_letters_guessed(letter_guessed, old_letters_guessed)

        if good_guess and letter_guessed.lower() in secret_word:
            if check_win(secret_word, old_letters_guessed):
                print(show_hidden_word(secret_word, old_letters_guessed))
                print(WINNER_MSG + " Good Job")
                break
        else:
            print(BAD_GUESS_STR)
            num_of_tries += 1
            print(HANGMAN_PHOTOS[num_of_tries])

        good_guess = False
        print(show_hidden_word(secret_word, old_letters_guessed))
    if num_of_tries > MAX_TRIES:
        print(LOSER_MSG)

def main():
    hangman("shain")

if __name__ == "__main__":
    main()

msg= input("Thank you for playing :) ")
	
