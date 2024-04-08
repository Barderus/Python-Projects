'''
    Build a vocabulary builder application that allows users to:
        * add new words
        * look up definitions
        * quiz themselves
        * track their progress. 
    Use dictionaries to store word-definition pairs and sets to store words the user has already learned.
'''
import json

def main():
    # Call the menu() function that displays the menu and get user choice
    ex = {}
    user_answer = menu()
    
    
    if user_answer == 1:
        add_words(ex) # Call the add_words function
    elif user_answer == 2:
        quiz() # Call the quiz function
    elif user_answer == 3:
        check_progress() # Call the check_progress function
    else:
        exit()


def menu():
    
    print("Enter the number that correspond to the activity you would to perform:")
    print('''
          1. Add new words to your vocab builder.
          2. Quiz yourself and prove your knowledge.
          3. Check your progress.
          4. Exit''')
    
    # Try-Except block to check if the user input is a valid integer between 1 and 3
    while True:
        try:
            response = int(input("Option: "))
            if response == 1 or response == 2 or response == 3 or response == 4:
                return response
            else:
                raise TypeError        
        except TypeError:
            print("ERROR! You must enter a valid integr number between 1 and 3.")
    

def create_dict(key, value):
    '''
        This function has two parameters:
            * Key = Word
            * Value = Word's definition
            
        Save the dictionary on a file
    '''
    # Initialize the dictionary
    word_dictionary = {}
    with open("vocab_builder.txt", "a", encoding= "utf-8") as file:
        if key in word_dictionary:
            print("Error! This word already exists in the dictionary.")
        else:
            word_dictionary[key] = value 
        json.dump(word_dictionary, file)
        
    return value

    
def add_words(ex):
    '''
        This function create a dicionary entry by calling the create_dict function and passing the word and definition as parameters
    '''
    #answer = "y"
    #while answer == "y":
    print("Add your new word!")
    word = input("Enter a word: ")
    definition = input("Enter the word definition: ")
        
        
    val = create_dict(word, definition)
    ex[val] = definition
    for x in ex.keys():
        pass
        #print("}{x + ex[x], end ="")
    answer = input("\nWould you like to enter another word? (Y/N) ").lower()
    
    if answer == "y":
        add_words(ex)
    else:
        return ex
        
def quiz():
    
    print("Prepare for your quiz!")
    with open("vocab_builder.txt", "a", encoding= "utf-8") as file:
        data  = json.load(file)
    print(data[2])


def check_progress():
    print("Getting your data ready...")


main()