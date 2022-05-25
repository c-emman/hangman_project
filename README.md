# Hangman Project
This projects aim was to create a Hangman game, where the user would input letters to guess a random word and would lose after a given number of tries

## Milestone 1
- The beginning milestone for this project focused on defining the necessary classes, functions, what attributes would be required and getting a base understanding of how the code would look like
- The second step in this milestone involved forming the first function in hangman class, ask_letter. This function when called would ask the user to input a letter, ensure the letter is a character and is only a single character. Upon entering a single character the letter would be checked in the list of previously entered letters to ensure the same letter couldn't be guessed multiple times. If this was a new character, the function would then call another function (check_letter), to check whether the letter was in the word.

>>> python
>>>     def ask_letter(self):

        while True:
            letter = input("Enter a single character: ")
            if len(letter) > 1:
                print("Please, enter just one character")
            elif len(letter) == 1:
                if letter in self.list_letters:
                    print(letter, "was already tried")
                else: 
                    self.check_letter(self, letter)
            else:
                print("Please enter a character")
            break
        pass
