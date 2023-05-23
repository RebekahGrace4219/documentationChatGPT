import random


class Hangman:
    def __init__(self, word_list, max_guesses):
        self.word_list = word_list
        self.max_guesses = max_guesses
        self.guessed_letters = []
        self.tries = max_guesses
        self.secret_word = ""

    def play(self):
        self.select_secret_word()
        self.display_initial_state()

        while self.tries > 0:
            guess = self.get_guess()

            if not self.is_valid_guess(guess):
                continue

            self.record_guess(guess)

            if self.is_correct_guess(guess):
                self.handle_correct_guess()
            else:
                self.handle_incorrect_guess()

            self.display_word()

            if not "_" in self.display_word():
                print("Congratulations! You won!")
                return

        print("Game over! The word was:", self.secret_word)

    def select_secret_word(self):
        self.secret_word = random.choice(self.word_list)

    def display_initial_state(self):
        print("Let's play Hangman!")
        print("_ " * len(self.secret_word))

    def get_guess(self):
        return input("Enter a letter: ").lower()

    def is_valid_guess(self, guess):
        if len(guess) != 1:
            print("Please enter a single letter.")
            return False

        if guess in self.guessed_letters:
            print("You already guessed that letter.")
            return False

        return True

    def record_guess(self, guess):
        self.guessed_letters.append(guess)

    def is_correct_guess(self, guess):
        return guess in self.secret_word

    def handle_correct_guess(self):
        print("Correct guess!")

    def handle_incorrect_guess(self):
        self.tries -= 1
        print("Incorrect guess! You have", self.tries, "tries left.")
        self.draw_hangman(self.tries)

    def draw_hangman(self, tries):
        stages = [
            '''
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            ''',
            '''
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     /
               -
            ''',
            '''
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |
               -
            ''',
            '''
               --------
               |      |
               |      O
               |     \\|
               |      |
               |
               -
            ''',
            '''
               --------
               |      |
               |      O
               |      |
               |      |
               |
               -
            ''',
            '''
               --------
               |      |
               |      O
               |
               |
               |
               -
            ''',
            '''
               --------
               |      |
               |
               |
               |
               |
               -
            '''
        ]
        print(stages[tries])

    def display_word(self):
        display_word = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        return display_word


word_list = ["hangman", "python", "game", "play"]
max_guesses = 6

hangman_game = Hangman(word_list, max_guesses)
hangman_game.play()
