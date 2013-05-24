# Name: Tyler Brown
# Section: 
# 6.189 Project 1: Hangman template
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "/home/ty/workspace/a_python_class/Projects/Project 1: Hangman/words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
 
letters_guessed = []

# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    ####### YOUR CODE HERE ######
    guess = True
    letter = 0
    for i in range(len(secret_word)):
        if secret_word[letter] not in letters_guessed:
            guess = False
            break
    return guess
        
    
def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed
    
    ####### YOUR CODE HERE ######
    word = []
    for letter in range(len(secret_word)):
        if secret_word[letter] not in letters_guessed:
            word.append('_')
        elif secret_word[letter] in letters_guessed:
            word.append(secret_word[letter])
    return word

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    # Update secret_word. Don't uncomment this line until you get to Step 8.
    secret_word  = get_word()

    ####### YOUR CODE HERE ######
    winner = False
    n = 6 #how many guesses are left???
    letter_guess = 0 #what letter did they guess?
    #continually loop:
    while n > 0 and winner == False:
        #print ''n guesses left ''
        n -= mistakes_made
        print "\n", n, "guesses left..."
        #print ''word''
        print print_guessed()
        #get letter in lowercase
        letter_guess = raw_input("Choose a letter:")
        letter_guess = lower(letter_guess)
        #check - has letter already been guessed
        if letter_guess in letters_guessed:
            print "Blow me over and tip me upright!"\
                  " you've already guessed that letter..."
        #check - is letter not in word?
        elif letter_guess not in secret_word:
            letters_guessed.append(letter_guess)
            print "Bloody baroque barbells! That's not"\
                  " in my secret word!!"
            mistakes_made += 1
        #check - is letter in word?
        elif letter_guess in secret_word:
            letters_guessed.append(letter_guess)
            print "Nice guess...aha! moments are nice"
            if word_guessed() == True:
                winner = True
    
    #game ending -- notice    
    print "whooahahahahaa!!!!!"
    if winner == True:
        print "you won!"
    else:
        print "you lost :-("    
   
#Test

play_hangman()