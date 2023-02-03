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