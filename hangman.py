import sys, random
from words import word_list
from time import sleep

class Hangman(object):
    # picks random word from word file
    def get_word(self):
        word = random.choice(word_list)
        return word.upper()

    # main game loop
    def play(self, word):
        word_completion = "_" * len(word)   # hidden letters in underscores
        guessed = False
        guessed_letters = []    # stores guessed letters
        guessed_words = []      # stores guessed words
        tries = 6               # 6 tries (according to length of stages)
        print("Let's play Hangman!")
        print(self.displayHangman(tries))
        print(word_completion)
        print("\n")
        while not guessed and tries > 0:
            print("Guessed so far: {}".format(str(guessed_letters)))
            guess = input("Please guess a letter or word: ").upper()
            # check if guess is a letter
            if len(guess) == 1 and guess.isalpha():
                # was the letter already guessed
                if guess in guessed_letters:
                    print("You already guessed the letter {}.".format(guess))
                # or was it not the right letter
                elif guess not in word:
                    print(guess, "is not in the word.")
                    tries -= 1
                    guessed_letters.append(guess)
                # or was it the right letter
                else:
                    print("Good job, {} is in the word!".format(guess))
                    guessed_letters.append(guess)
                    # now alter the underscores to display the correctly guessed letter(s)
                    word_as_list = list(word_completion)                              # converts underscores to list
                    indices = [i for i, letter in enumerate(word) if letter == guess] # enumerates the WORD and checks which letter(s) matches guess, and saves the index of the letter(s)
                    for index in indices:
                        word_as_list[index] = guess             # replaces corresponding index(es) in underscore with the letter(s)
                    word_completion = "".join(word_as_list)     # converts it back to string
                    if "_" not in word_completion:
                        guessed = True
            # check if guess is a word
            elif len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words:
                    print("You already guessed the word {}.".format(guess))
                elif guess != word:
                    print("{} is not the word.".format(guess))
                    tries -= 1
                    guessed_words.append(guess)
                else:
                    guessed = True
                    word_completion = word
            # if none of the above, it's invalid
            else:
                print("Not a valid guess")

            # diplays updated hangman
            print(self.displayHangman(tries))
            print(word_completion)
            print("\n")

        if guessed:
            print("Congrats, you guessed the word! You win!")
        else:
            # making it sleep to make it more dramatic..
            print("Sorry, you ran out of tries.")
            sleep(1.5)
            print("The word was {}.".format(word))
            sleep(1.5)
            print("Maybe next time...")
            sleep(1.5)

    # 7 tries (1 head, 2 arms, 2 legs, 1 core) aka len of list
    def displayHangman(self, tries):
        stages = ["""
                    ---------
                    |       |
                    |       O
                    |      \\|/
                    |       |
                    |      / \\
                    """,
                    """
                    ---------
                    |       |
                    |       O
                    |      \\|/
                    |       |
                    |      / 
                    """,
                    """
                    ---------
                    |       |
                    |       O
                    |      \\|/
                    |       |
                    |
                    """,
                    """
                    ---------
                    |       |
                    |       O
                    |      \\|
                    |       |
                    |
                    """,
                    """
                    ---------
                    |       |
                    |       O
                    |       |
                    |       |
                    |
                    """,
                    """
                    ---------
                    |       |
                    |       O
                    |
                    |
                    |
                    """,
                    """
                    ---------
                    |       |
                    |
                    |
                    |
                    |
                    """
                    ]
        return stages[tries]

def main():
    hh = Hangman()
    word = hh.get_word()
    hh.play(word)
    # runs while the input == y, else it prints goodbye message
    while input("Play Again? (Y/N) ").upper() == "Y":
        print()     # just to space things out a bit
        word = hh.get_word()
        hh.play(word)
    print(random.choice(["Goodbye", "Adios", "Sayonara", "Peace out", "Ciao", "Slan abhaile", "See ya"]))

if __name__ == '__main__':
    main()
