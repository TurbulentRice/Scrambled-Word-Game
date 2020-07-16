from scrambled import Scrambled

'''
DEFAULT START GAME

my_game = Scrambled()

'''

#   MAIN MENU
#   my_language allows a lang other than 'eng' be passed to objects' constructors in future
my_language = 'eng'    #    input("Language: ")

#   Load game but don't start
my_game = Scrambled(my_language, start=False)

while True:
    print('''Main Menu:
    1) Play 'Scrambled'
    2) Lookup a word
    3) Randomonium
    4) Test vocab
    5) Quit''')
    choice = input("Select: ").strip().lower()

    if ("play" in choice) or ("1" in choice):
        #   Start game
        my_game.intro()

    elif ("look" in choice) or ("2" in choice):
        while True:
            a_word = input("Word to lookup: ")
            print(my_game.vocab.get_def(a_word))
            c = input("Another? (y/n): ")
            if "n" in c.lower():
                break

    elif ("rand" in choice) or ("3" in choice):
        while True:
            #   Return a random word of any length (excluding no chars), and its definition
            rand_word, definition = my_game.vocab.get_rand_word(r_val=True)
            print(rand_word + ": " + definition)
            c = input("Another? (y/n): ")
            if "n" in c.lower():
                break

    elif ("test" in choice) or ("4" in choice):
        my_game.test()

    elif ("quit" in choice) or ("5" in choice):
        print("Bye!")
        break

