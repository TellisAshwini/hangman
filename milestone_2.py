import random
word_list = ['Apple', 'Plum', 'Grapes', 'Orange', 'Pineapple']
print(word_list)
word = random.choice(word_list)
print(word)


guess = input('Please enter a single letter here: ')
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")