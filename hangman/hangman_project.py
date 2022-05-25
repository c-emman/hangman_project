import random

hangman_list = [
"""      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___
    
        H A N G M A N""",
"""      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___
    
        H A N G M A _""",
"""      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___
    
        H A N G M _ _""",
"""      _______
     |/      |
     |      (_)
     |      \|
     |       |
     |      
     |
    _|___
    
        H A N G _ _ _""",
"""      _______
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
    _|___
    
        H A N _ _ _ _""",
"""      _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___
    
        H A _ _ _ _ _""",
"""      _______
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___
    
        H _ _ _ _ _"""]


class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.list_letters = []

        print(hangman_list[self.num_lives])
        print("The mystery word has", len(self.word), "characters")
        print(self.word_guessed)
        print("You have", num_lives, "lives.")
        pass

    def check_letter(self, letter) -> None:

        if letter.lower() in self.word:
            for i, char in enumerate(self.word):
                if letter.lower() == char:
                    self.word_guessed[i] = letter.lower()
                    self.num_letters -= 1
                    print("Nice!", letter, "is in the word!")
                    self.list_letters.append(letter.lower())
                    continue
                else:
                    continue
            print(self.word_guessed)    
        else:
            self.num_lives -= 1
            self.list_letters.append(letter.lower())
            print("Sorry,", letter, "is not in the word.")
            print(hangman_list[self.num_lives])
            print("You have", self.num_lives, "lives left.")


    def ask_letter(self):

        while True:
            letter = input("Enter a single character: ")
            if len(letter) > 1:
                print("Please, enter just one character")
            elif len(letter) == 1:
                if letter in self.list_letters:
                    print(letter, "was already tried")
                else: 
                    self.check_letter(letter)
            else:
                print("Please enter a character")
            break
        pass

def play_game(word_list):
    game = Hangman(word_list, num_lives=6)
    
    while game.num_lives >= 0:
        if game.num_lives > 0 and '_' in game.word_guessed:
            game.ask_letter()
        elif game.num_lives > 0 and '_' not in game.word_guessed:
            print("Well done! You've beaten the game")
            print("The word was", ''.join(game.word))
            break
        elif game.num_lives == 0:
            print("You're out of lives! Better luck next time")
            print("The word was", ''.join(game.word))
            break
    pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
