# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "/Users/ouyangtianna/Desktop/hangman/words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    result = True
    for i in secret_word:
        if i not in letters_guessed:
            result = False
            break
    return result



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    tem = ''
    for i in secret_word:
        if i in letters_guessed:
            tem += i
        else:
            tem += '_ '
    return tem



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    temp1 = string.ascii_lowercase
    temp2 = ''
    for i in temp1:
        if i not in letters_guessed:
            temp2 += i
    return temp2
    
    

def hangman():
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word = choose_word(load_words())
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is '+str(len(secret_word))+' letters long.')
    guess = 6
    vowel = ['a','e','i','o','u']
    letters_guessed = []
    warnings_left = 3
    print('You have ' + str(warnings_left) +' warnings left.')
    unique_words = 0
    tem = []
    for i in secret_word:
        if i not in tem:
            tem.append(i)
            unique_words += 1    
    
    while guess > 0:
        print('-----------------')
        print('You have '+str(guess)+' guesses left.')
        available_letters = get_available_letters(letters_guessed)
        print('Available letters: '+ available_letters)
        user_guess = input('please guess a letter: ')
        if warnings_left > 0:
            if str.isalpha(user_guess) == True:
                if user_guess not in letters_guessed:
                    new_guess = str.lower(user_guess)
                    if new_guess not in vowel:
                        guess -= 1
                    else:
                        guess -= 2
                    letters_guessed.append(new_guess)        
                    result = is_word_guessed(secret_word, letters_guessed)
                    if result == True:
                        print('Congratulations, You won!')
                        break
                    else:              
                        if new_guess in secret_word:
                            print("Good guess: "+ get_guessed_word(secret_word, letters_guessed))
                        else:
                            print("Opps! That letter is not in my word: "+ get_guessed_word(secret_word, letters_guessed))
                else:
                    warnings_left -= 1
                    print("Opps! You've already guessed that letter. You have "+ str(warnings_left)+' warnings left: '+ get_guessed_word(secret_word, letters_guessed))
                
            else:
                warnings_left -= 1
                print('Opps! That is not a valid letter. You have '+ str(warnings_left)+' warnings left: '+get_guessed_word(secret_word, letters_guessed))
        else:
            if str.isalpha(user_guess) == True:
                if user_guess in letters_guessed:
                    print("Opps! You've guessed that letter. You have no warnings left")
                    print('so you lose one guess: '+ get_guessed_word(secret_word, letters_guessed))
                    guess -= 1
            if str.isalpha(user_guess) == False:
                print("That is not a valid letter. You have no warnings left")
                print("so you lose one guess: "+ get_guessed_word(secret_word, letters_guessed))
                guess -=1
    if result == True:
        total_score = guess*unique_words
        print('Your total score for this game is: '+str(total_score))    
    else:
        print("Sorry, you ran out of guesses. The word was else: "+secret_word)                

            
#hangman()
        


            
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(" ","")
    result = True
    for i in range(len(my_word)):
        if str.isalpha(my_word[i]) == True:
            if not len(my_word) == len(other_word):
                result = False
                break
            else:
                if not my_word[i] == other_word[i]:
                    result = False
                    break
    return result    
                
match_with_gaps('te_ t','tact')    
match_with_gaps("a_ _ le","banana")    
match_with_gaps("a_ _ le","apple")    
match_with_gaps('a_ ple', 'apple')




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    wordlist = load_words()
    my_word = my_word.replace(" ","")
    newlist = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            newlist.append(word)
    if not newlist:
        print('No matches found')
    else:
        for word in newlist:
            print(word, end = " ")

#show_possible_matches("a_ pl_ ")



def hangman_with_hints():
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    secret_word = choose_word(load_words())
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is '+str(len(secret_word))+' letters long.')
    guess = 6
    vowel = ['a','e','i','o','u']
    letters_guessed = []
    warnings_left = 3
    print('You have ' + str(warnings_left) +' warnings left.')
    unique_words = 0
    tem = []
    for i in secret_word:
        if i not in tem:
            tem.append(i)
            unique_words += 1    
    
    while guess > 0:
        print('-----------------')
        print('You have '+str(guess)+' guesses left.')
        available_letters = get_available_letters(letters_guessed)
        print('Available letters: '+ available_letters)
        user_guess = input('please guess a letter: ')
        if warnings_left > 0:
            if str.isalpha(user_guess) == True:
                if user_guess not in letters_guessed:
                    new_guess = str.lower(user_guess)
                    if new_guess not in vowel:
                        guess -= 1
                    else:
                        guess -= 2
                    letters_guessed.append(new_guess)        
                    result = is_word_guessed(secret_word, letters_guessed)
                    if result == True:
                        print('Congratulations, You won!')
                        break
                    else:              
                        if new_guess in secret_word:
                            print("Good guess: "+ get_guessed_word(secret_word, letters_guessed))
                        else:
                            print("Opps! That letter is not in my word: "+ get_guessed_word(secret_word, letters_guessed))
                else:
                    warnings_left -= 1
                    print("Opps! You've already guessed that letter. You have "+ str(warnings_left)+' warnings left: '+ get_guessed_word(secret_word, letters_guessed))
            elif user_guess == '*':
                print("Possible word matches are: ")
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            else:
                warnings_left -= 1
                print('Opps! That is not a valid letter. You have '+ str(warnings_left)+' warnings left: '+get_guessed_word(secret_word, letters_guessed))
        else:
            if str.isalpha(user_guess) == True:
                if user_guess in letters_guessed:
                    print("Opps! You've guessed that letter. You have no warnings left")
                    print('so you lose one guess: '+ get_guessed_word(secret_word, letters_guessed))
                    guess -= 1
            if str.isalpha(user_guess) == False:
                print("That is not a valid letter. You have no warnings left")
                print("so you lose one guess: "+ get_guessed_word(secret_word, letters_guessed))
                guess -=1
    if result == True:
        total_score = guess*unique_words
        print('Your total score for this game is: '+str(total_score))    
    else:
        print("Sorry, you ran out of guesses. The word was else: "+secret_word)                


hangman_with_hints()
