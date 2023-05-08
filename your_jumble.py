# Ben Sabler
# SUNY Cobleskill - Winter Session 2021
# Guess My Number
# This program demonstrates the ability to open, read and write to/from
# a text file and implementing a game loop.

# Importing the random module allows us to use the random
# choice method to select a word from the word pool.
import random

# Defines a function that takes a paramater we're calling 'file' that we'll
# use to pass a text file that will be open and read.
def get_the_list_of_words(file):
    # We initialize a variable 'text_file' that stores the value of the
    # text file contents. We achieve this by using the open method and pass two
    # paramaters, the file paramater, and the mode 'r' which allows us to read the file.
    text_file = open(file, "r")
    # We initialize a variable 'words' with the data type of list, so that we can hold the contents of the text file.
    words = []
    # We initialie a variable 'word' and we store inside it the first line of the file, while
    # simultaneously replacing the default escape character with a blank string, thus removing it.
    word = text_file.readline().replace("\n", "")
    # We initialize a loop that runs under the condition that the length of the word
    # variable is greater than 0.
    while len(word) > 0:
        # In each iteration of the loop, we append to the words variable the value of the word variable.
        words.append(word)
        # In addition to each append, we also replace the escape character with an empty string.
        word = text_file.readline().replace("\n", "")
    # When the loop is done, we are done with the file and we must close it, using the appropriate method.
    text_file.close()
    # Now that we are done storing the words from the text file to the list, we return that list.
    return words

# Defines a function that simply displays the game instructions.
def print_instructions():
    # This print statement displays the instructions to the game.
    print("""
        Welcome to the Word Jumble
        
        Unscramble the letters to make a word.
        
        """)

# Defines a function thattakes a paramter we're calling 'words' that we're going to
# pass the list of words so that we can make a random selection from.
def pick_a_word(words):
    # We are initializing a variable 'word' that we are storing a string value
    # which will have a method performed from the random module 
    # random.choice which we pass the variable we used as the paramater for
    # the function.
    word = random.choice(words)
    # We take the variable we passed in the function as the paramter and 
    # we then remove the randomly selected word.
    words.remove(word)
    # We then return the randomly selected word and the updated list.
    return word, words

# Defines a function that takes a paramter we are calling 'word' that will be used
# for string manipulation in an effort to rearrange the character order.
def jumble_the_word(word):
    # We initialize an empty string variable called 'jumble'.
    jumble = ""
    # We initliaze a loop under the condition that the variable we passed as the paramter
    # of the function remains 'True'.
    while word:
        # We initialize a variable called 'position' which stores the value
        # of a random index value of the provided word. The value can only
        # be the range of the length of the word.
        position = random.randrange(len(word))
        # We take the jumble variable and we append to it the character
        # at whatever index value the position variable is storing at the 
        # current iteration.
        jumble += word[position]
        # At the end of every iteration we take the variable we passed as a paramater to the 
        # function and we store a concatenation inside it the value of the character from the beginning
        # to the current index value inside the position variable and also the character from the
        # index value of the position variable + 1 to the end.
        word = word[:position] + word[(position + 1):]
    # We then return the new string value stored in the jumble variable.
    return jumble

# Defines a function that takes a paramter we are calling 'correct' which stores the string
# value of the correct unjumbled string value.
def guessing_loop(correct):
    # We initialize a variable called 'guess' that stores a string value which is prompted
    # from the user. An escape character is used to move to a new line for the user to 
    # type their guess.
    guess = input("\nYour guess: ")
    # We initialize a loop under the condition that the value stored in the guess variable
    # does not equate to the string value in the paramater passed to the function and also
    # the guess variable is an empty string.
    while guess != correct and guess == "":
        # We tell the user that their guess is incorrect.
        print("Sorry, that's not it.")
        # We then prompt them to guess again,
        guess = input("Your guess: ")
    # We create a conditional statement that if the string value in guess variable equates to
    # the string value in the passed paramater, we return a boolean value True.
    if guess == correct:
        return True
    else:
        # Otherwise we return the boolean value False, however we should not reach this code block if the 
        # user is being prompted.
        return False

# Defines the main playing loop function that takes a paramter we call 'words' that takes the current
# list of words.
def playing_loop(words):
    # We initialize a variable valled 'response' and set the initial value to 'y'.
    response = "y"
    # We initialize a loop that runs under the condition that while the response variable equates to 'y'
    # which has the lower method performed on it to ensure we have the lower case character
    # and the length of the paramater we passed to the function is true.
    while response.lower() == "y" and len(words):
        # We initialize a variable word and take the variable we passed as the paramater to the function
        # and store the value to it the function we defined earlier in the program, pick_a_word and pass the paramater
        # to this function the same variable we passed to this playing loop function.
        word, words = pick_a_word(words)
        # We initialize the variable jumble and store the value inside it the function we defined earlier
        # in the program jumble_the_word and pass the word variable to it as the paramater.
        jumble = jumble_the_word(word)
        # We print to the console what the jumbled word to be unscrambled will be.
        print("\n\nThe jumbe is: ", jumble)
        # We create a conditional statement that if the function we defined earlier in the program
        # guessing_loop evaluates to true.
        if guessing_loop(word):
            # We then print to the user that they have guessed correctly.
            print("That's it! You guessed it!\n")
            # We then prompt the user if they'd like to play again, and store the new value inside the response
            # variable we initialized at the beginning of this function.
            response = input("Play again? ")

# Defines a function that takes two paramaters we call 'file' and 'words', that we use to write
# the words that were unused back to a text file.
def write_remaining_words(file, words):
    # We initialize a variable called 'text_file' and store the value to it the open function and pass
    # to it a paramater that is the same variable we received as he paramater to this function, and
    # we use the mode 'w' that indicates we are writing to the file.
    text_file = open(file, "w")
    # We create  conditional satement that if the length of the paramater variable 'words' equates
    # to zero.
    if len(words) == 0:
        # We print a statement to the user that there are no words to write.
        print("\n\nSorry... there are no more words.")
    else:
        # Otherwise we initialize a loop that iterates through the length of the words variable.
        for i in range(len(words)):
            # For every iteration we use the write method on the text_file variable and write to the
            # text file the word wherever the index value is in the loop.
            text_file.write(words[i])
            # We also include an escape character after every word to create a new line after every
            # word written to the file.
            text_file.write("\n")
    # When we are done writing the unused words to the text file, we close the file.
    text_file.close()

# Defines a function that prints to the console statements thanking the user and saying goodbye.
def say_goodbye():
    print("\nThanks for playing.")
    input("\n\nPress the enter key to exit.")

# Calls the print_instructions function we defined.
print_instructions()
# We initialize a global variable called 'file_source' and we store the value of the
# directory location of our text file that contains our word pool.
file_source = "WordJumble/word_pool_source.txt"
# We initialize a global variable called 'file_destination' and we store the value of the
# directory location of our text file that we write our unused words into.
file_destination = "WordJumble/word_pool_destination.txt"
# We initialize a global variable called 'words' and we store the value of the
# function that was defined earlier get_the_list_of_words and pass the file_source
# variable to it as its paramater.
words = get_the_list_of_words(file_source)
# We call the playing_loop function and pass the global variable words to it as its paramater.
playing_loop(words)
# We call the write_remaining_words function and pass the global variable file_destination and words to it as its paramater.
write_remaining_words(file_destination, words)
# Lastly, we call the say_goodbye function we defined earlier in the program.
say_goodbye()