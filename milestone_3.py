import random
word_list = ['Apple', 'Plum', 'Grapes', 'Orange', 'Pineapple']
word = random.choice(word_list)

def check_guess():
    while True:
        try:
            guess = input('Please enter a single letter here: ')
            if len(guess) == 1 and guess.isalpha():
                break
            else:
                raise Exception
        except:
            print("Invalid letter. Please, enter a single alphabetical character.")
    if guess.lower() in word.lower():
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')