
#test
import string 
secret_word = 'claptrap'
letters_guessed = ['c','l','x','r','t','p','x','p']

def word_guessed(secret_word, letters_guessed):
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    
    ####### YOUR CODE HERE ######
    word = []
    for letter in range(len(secret_word)):
        if secret_word[letter] not in letters_guessed:
            word.append('_')
        elif secret_word[letter] in letters_guessed:
            word.append(secret_word[letter])
    return word
        
              
#test function

print word_guessed(secret_word, letters_guessed)