import random
from words import sample_words #imported module from other file :))
from design_of_the_game import My_visuals  # imported module from other file :))
import string


def get_valid_word(sample_words):
    word = random.choice(sample_words)
    while '-' in word or ' ' in word:
        word = random.choice(sample_words)

    return word.upper()


def hangman():
    word = get_valid_word(sample_words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 8

    # user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(My_visuals[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  #life of the user
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter idiot, guess another.')

        else:
            print('\nThat is not a valid letter.')

    # trigger if lives = 0
    if lives == 0:
        print(My_visuals[lives])
        print('You died, sorry broskie. The word was', word)
    else:
        print('Congratulations my dude! You guessed the word', word, '!!')

if __name__ == '__main__':
    hangman()