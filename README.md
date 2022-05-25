# Hangman Project
This projects aim was to create a Hangman game, where the user would input letters to guess a random word and would lose after a given number of tries. The technology used in this project was Python and also used the random module.

## Milestone 1
- The beginning milestone for this project focused on defining the necessary classes, functions, what attributes would be required and getting a base understanding of how the code would look like
- The second step in this milestone involved forming the first function in hangman class, ask_letter(). This function when called would ask the user to input a letter, ensure the letter is a character and is only a single character. Upon entering a single character the letter would be checked in the list of previously entered letters to ensure the same letter couldn't be guessed multiple times. If this was a new character, the function would then call another function check_letter(), to check whether the letter was in the word.

>>> python
```python
    def ask_letter(self):

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
```
## Milestone 2
- This milestones focus was to properly define the class for the game hangman, the inputs into the class and the attributes. This required some conderation as to what potential attributes the class could have and the initial values for these attributes. The required inputs for the game where the word list and the number of lives available to the player
- Some conderation was also needed to know how the computer would use a random word from the word list, how the word_guessed attribute would be formed and other less attributes which would be needed for the running of the game.
- Below is the code made to define the class of the game Hangman:

>>> python
```python
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
```
## Milestone 3
- This milestone focused on the check_letter() function. This function needed to check whether the letter was in the word to be guessed; if yes the letter needed to be replaced in the relevant position and the rest of the letter sremain un-guessed, however if incorrect the number of lives needs to be reduced by 1 and let the user know the letter was incorrect. In both cases the letter needed to be added to the list of letters which had been guessed to ensure the same letter was not guessed multiple times. 
- This function also needed to work together with the ask_letter() function as this would be called in that function
- See the code below:

>>> python
```python
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
```
## Milestone 4
- The final milestone focused on puting it all together. At this point the relevant sections of the class had been filed and all that was left was to define a final function outside the class that would loop the game until the condition of either the player running out of lives or the player fully guessing the word had been reached.
- See below the function play_game():
>>> python
```python
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
```
- Once this milestone was complete now additions could be added to the game. I added a diagram of the hangman which would spell hangman once the player had lost the game.

> ![ksnip_20220525-153427](https://user-images.githubusercontent.com/105006854/170288044-34a48fb6-dc14-46a6-8131-d8f1bdefae00.png)

## Conclusion
To conclude this project worked on numerous python concepts such as classes, methods, functions, control flow and manipulation of strings, lists and loops. 
