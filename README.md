# Scrambled-Word-Game
Word guessing game based around Webster's English Dictionary.

Player is given a string of random letters, has three tries to guess the word correctly.
Scoring based on selected difficulty level and tries remaining.
Five levels, guess all correctly to win.

Includes Dictionary class which deserializes JSON file to Python dict 'vocabulary', moves undesired words to dict 'trash'.

main.py provides an interface for accessing the basic methods of Dictionary and Scrambled objects, however, all that is needed to play Scrambled is to instantiate a default Scrambled objcet:

my_game = Scrambled()
equivalent to:
my_game = Scrambled(lang='eng', test=False, start=True)
