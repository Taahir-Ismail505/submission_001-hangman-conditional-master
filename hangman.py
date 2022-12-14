import random

#from typing_extensions import runtime


def read_file(file_name):
    '''
    opens and reads file of your choice
    '''
    file = open(file_name,'r')
    return file.readlines()


def select_random_word(words):
    '''
    selects random word from  the txt file user has open
    '''
    random_index = random.randint(0, len(words)-1)
    word = words[random_index]
    return word


def select_random_letter_from(word):
    '''
    takes a random letter from the selected word and hides the character with underscore
    then returns the random number and letter
    '''
    random_index = random.randint(0, len(word) - 1)
    letter = word[random_index]
    print('Guess the word: ' + word[:random_index] + "_" + word[random_index+1:])
    return letter, random_index


def get_user_input():
    '''
    gets input to compare with word
    '''
    return input('Guess the missing letter: ')


def show_answer(answer, selected_word, missing_letter_index):
    """
    TODO Step 1 - Show better results messages
    """
    '''
    compares your answer with original and checks if its correct ..based on tht displays 
    if its right or wrong
    '''
    wordFull = selected_word
    if list(selected_word)[missing_letter_index]== answer :
        print("The word was: "+ selected_word)
        print("Well done! You are awesome!")
    else:
        print("The word was: "+ selected_word)
        print("Wrong! Do better next time.")
    pass


# TODO: Step 2
def ask_file_name():
    """
    TODO Step 2 - Update to prompt user for filename to use for words
    """

    '''
    asks if the user would like to pull words from another txt file
    '''
    wordlist = input("Words file? [leave empty to use short_words.txt] :")
    if wordlist == '':
        return 'short_words.txt'
    return wordlist
    
    




def run_game(file_name):
    """
    You can leave this code as is, and only implemented above where the code comments prompt you.
    """
    '''
    runs all functions
    '''
    words = read_file(file_name)
    word = select_random_word(words)
    missing_letter, letter_index = select_random_letter_from(word)
    answer = get_user_input()
    show_answer(answer, word, letter_index)


if __name__ == "__main__":
    words_file = ask_file_name()
    run_game(words_file)

