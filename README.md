# Scrambled-Word-Game
Word guessing game based on top of Webster's English Dictionary (WED).

Rules/Features:
Words are randomly selected from WED
Player is given a string of scrambled letters, has three tries to guess the word correctly.
Five levels (words) of increasing difficulty (length), guess all correctly to win.
Scoring based on selected game difficulty and tries remaining.
High score saved between games played within the same Scrambled object.

Features:
  - "main.py" provides an interface for accessing the basic methods of Dictionary and Scrambled objects.
  - "Scrambled" class manages game, interacts with Dictionary object attribute
  - "Dictionary" class deserializes JSON file to Python dict 'vocabulary', moves undesired words to dict 'trash'. Performs actions over WED for return to Scrambled.
  - WED JSON file (~25mb)
  
All that is needed to play Scrambled is to instantiate a default Scrambled objcet:
my_game = Scrambled()
equivalent to:
my_game = Scrambled(lang='eng', test=False, start=True)
