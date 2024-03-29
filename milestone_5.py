import random #To generate random words from the list of words.

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        #Generates random word from the word_list.
        self.word               = random.choice(word_list) 
        #A list of the letters of the word, with _ for each letter not yet guessed.
        self.word_guessed       = ['_'] * len(self.word) 
        #Number of the unique letters in the word to be guessed.
        self.num_letters        = len(set(self.word))
        #Number of lives a player has.
        self.num_lives          = num_lives 
        #A list of words.
        self.word_list          = word_list
        #A list of the letters that have been guessed.
        self.list_of_guesses    = [] 
        print(f'The mistery word has {self.num_letters} characters')
        print(self.word_guessed)

    def check_guess(self, guess):
        #Checks if the guessed letter is in the word.
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for index, letter in enumerate(self.word):
                if guess == letter:  
                    self.word_guessed[index] = guess #Replaces the '_' with the letter guessed correctly.
            self.num_letters -= 1  #Number of letters reduces each time the letter is guessed correctly.
            print(self.word_guessed)
        else:
            self.num_lives -= 1  #Number of lives reduces each time the letter is guessed wrong.
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')
            #Appends the unique letters guessed to list_of_guesses.
        self.list_of_guesses.append(guess) #Appends the unique letters guessed to list_of_guesses.

    def ask_for_input(self):
        #Asks user to guess the letter and checks if the entered character is a single alphabet.
        while True:
            guess = input('Please enter a single letter here: ')
            guess = guess.lower()
            if len(guess) != 1 or guess.isalpha() == False: #checks if the letter guessed is single alphabet
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:   #Checks if the letter is already guessed.
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0: #If the number of lives is equal to 0 then player loses the game.
            print('You lost!')
            break
        elif game.num_lives > 0: #If the number of lives are greater than 0 then continues the game.
            game.ask_for_input()
            if game.num_letters == 0:  #If all the letter are guessed the player wins.
                print('Congratulations. You won the game!')
                break



word_list = ['apple', 'avocado', 'banana','blueberry', 'blackberry','cherry',  'cranberry', 'dragonfruit', 
    'grapefruit', 'grape', 'jackfruit','kiwi', 'lychee', 'lemon', 'mangosteen', 'muskmelon', 'mango', 
    'orange', 'pineapple', 'pear', 'pomegranate', 'papaya','raspberry', 'rambutan','strawberry', 'tangerine',
    'watermelon']
play_game(word_list)

