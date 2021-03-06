from re import T
import random
import string
from words import choose_word
from images import IMAGES
'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the word correctly )
      return False (wrong selection) 
    '''
    for letter in  secret_word:
        for letter2 in letters_guessed:
            if letter == letter2:
                continue
            else:
                return False
    

    return True

# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''
    letters_left = string.ascii_lowercase
    
    for letter in letters_guessed:
        letters_left = letters_left.replace(letter , " " )
    
    return letters_left


def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')

    letters_guessed = []
    remaining_lives = 8
    wrong_guess_count = 0
    hint_count = 0
    while remaining_lives > 0:
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {} ".format(available_letters))
        guess = input("Please guess a letter: ")
       
         
    

        if hint_count < 1 and guess.lower() == "hint"  :
            hint_count += 1
            print("The Hint is : "+"".join(random.choice(secret_word)))
            continue
            
        else:
            flag = ifValid(guess)
            if flag == False :
                print("Invalid Input")
                guess = input("Please guess a letter:")

        
        letter = guess.lower()

        if letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            if is_word_guessed(secret_word, letters_guessed) == True:
                print(" * * Congratulations, you won! * * ", end='\n\n')
        else:
            print("Oops! That letter is not in my word: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            wrong_guess_count += 1
            image(wrong_guess_count)
            remaining_lives -= 1
            if remaining_lives == 0:
                print("GAME OVER")
                
            letters_guessed.append(letter)
            print(f"Lives : {remaining_lives}/8")
            print("")
    
    

def image(wrong_guess_count):

    print(IMAGES[wrong_guess_count])

def ifValid(input_character):
 # condition : 
 #* input length == 1
 #* must be character from a-z
 #return :
 # true or false
    str = string.ascii_lowercase
    if len(input_character) == 1:
        for letter in str:
            if input_character == letter :
                return True

    return False           
                
            

# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
#secret_word = "hun"
hangman(secret_word)
