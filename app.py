import random
#variables
WORDS_LIST = ["green apple", " yellow banana", "cherry", "mango", "orange"]
MAX_TRIES = 5
RED = 31
GREEN = 32
YELLOW = 33
BLUE = 34
#init
def word_init(word_list: list[str])-> tuple[str, list]:
    """this func choose random word from words list and return the word and list that represent mask word"""
    word = random.choice(word_list)
    word_x = ["_"] * len(word)
    for i in range(len(word)):
        if word[i] == " ":
            word_x[i] = " "
    return word, word_x

#styling
def colorprint(text: str, color: int):
    print(f"\033[{color}m{text}\033[0m")
#cli methods

def show_word(word_x: list[str])-> None:
    """turning the list represent mask word to string and print it to user"""
    print(f"Word to guess: {"".join(word_x)}")
def show_tries(left_tries: int)-> None:
    print(f"Tries left: {left_tries}")
def get_char()-> str:
    return input("Enter char: ")
def success_message()-> None:
    colorprint("\nG-R-A-T-U-L-A-T-I-O-N-S-!\n You win the game", GREEN)
def fail_message()-> None:
    colorprint("\nG-O-O-D-B-Y-E   L-O-S-E-R..!\nMaybe next time", RED)
def separate()-> None:
    colorprint("*" * 40, YELLOW)

#logic methods
def in_word(char, word)-> bool:
    """check if a char is part of the word"""
    return char.lower() in word
def x_word_update(word_x, word, char)-> list[str]:
    """update the list of mask word by the char that was found"""
    for i in range(len(word)):
        if word[i] == char:
            word_x[i] = f"\033[{BLUE}m{char}\033[0m"
    return word_x
def word_complete(word_x)-> bool:
    """check if all chars in the word was found"""
    return not '_' in word_x
def valid_input(char, guessed_chars)-> bool:
    """validate that the input is only one alpha letter"""
    if not char.isalpha():
        print("ERROR: must be char")
        print("try again")
        return False
    elif len(char) > 1:
        print("ERROR: must be ONE char")
        print("try again")
        return False
    elif char in guessed_chars:
        print("you already guessed this char.")
        print("try again")
        return False
    return True

#app flow
def app(word_list, max_tries)-> None:
    """the flow of the program itself"""
    #init
    #guessed_chars to prevent duplicate chars tries
    guessed_chars = []
    word, word_x = word_init(word_list)
    left_tries = max_tries
    while left_tries > 0 and not word_complete(word_x):
        show_tries(left_tries)
        show_word(word_x)
        user_char = get_char()
        separate()

        if not valid_input(user_char, guessed_chars):
            separate()
            continue
        guessed_chars.append(user_char)
        if in_word(user_char, word):
            word_x = x_word_update(word_x, word, user_char)
        else:
            left_tries -= 1
    #end game
    if word_complete(word_x):
        show_word(word)
        separate()
        success_message()
    else:
        show_word(word)
        separate()
        fail_message()

#app
if __name__ == '__main__':
    app(WORDS_LIST, MAX_TRIES)

