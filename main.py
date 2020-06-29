from scrambled import Scrambled
#   Main program

#   Get language
my_language = 'eng'
#   Open game but don't start
my_game = Scrambled(my_language, start=False)

#   Main Menu
while True:
    print("Main Menu:\n1) Play 'Scrambled'\n2) Lookup a word\n3) Randomonium\n4) Test vocab")
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
            #   Return a random word of any length excluding no chars + its definition
            rand_word, definition = my_game.vocab.get_rand_word(r_val=True)
            print(rand_word + ": " + definition)
            c = input("Another? (y/n): ")
            if "n" in c.lower():
                break

    elif ("test" in choice) or ("4" in choice):
        my_game.test()

