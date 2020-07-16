import time
from dictionary import Dictionary, random

class Scrambled:
    def __init__(self, lang: str = "eng", test=False, start=True):

        #   Main Dictionary object
        self.vocab = Dictionary(lang)

        #   Difficulty 8 - 10, determines length of words in wordList
        self._difficulty = int(8)

        self._high_score = int(0)

        #   Sassy preloaded messages
        self.win_messages = ["Congratulations! Ya beat me fair and square.",
                    "You won't be so lucky next time...",
                    "Ok ok, you win this one.",
                    "How could I lose to a human!? Well played.",
                    "You won! Maybe I'll stop going easy...",
                    "Not bad... But I let you win."]

        self.lose_messages = ["You're no match for my machine intelligence!",
                     "Better luck next time...",
                     "You'll have to do better than that to beat me!",
                     "Nice try, but I won't be defeated that easily.",
                     "It's ok, soon AI will rule the world and you won't feel so bad about losing to me.",
                     "You lose! I'm the Scrambled champ! Next stop, Skynet..."]

        self.correct_messages = ["Wow! You got it on try #{}!",
                        "Lucky guess! Only took you {} tries.",
                        "Very good. You got it on try {}.",
                        "That one was easy... Everyone gets that one on try #{}.",
                        "You got it on try {}! The next one won't be so easy...",
                        "Beginner's luck. This one took you {} tries to get."]

        self.wrong_messages = ["I don't think so! Try again.",
                      "Is THAT your best guess? Try again.",
                      "Nope... Give it another shot.",
                      "Incorrect. Maybe this is too hard... Try again.",
                      "Incorrect! You'll have to step up your game. Try again.",
                      "*HAL 9000 voice* I'm sorry Dave, I'm afraid that is incorrect."]

        if test:
            self.test()
        if start:
            self.intro()

    #   Test vocab object
    def test(self):
        #   Test vocabulary
        self.line()
        print("Words in dictionary: ", self.vocab.get_size())
        print("Longest word: ", self.vocab.get_longest_word())
        print("Words in trash: ", len(self.vocab.trash))
        self.line()

    #   Format function, sleeps and prints lines
    @staticmethod
    def line(delay: float = 0, txt: str = "--------------------", r: int = 1):
        time.sleep(delay)
        #   Print line r times
        for i in range(r):
            print(txt)

    #   Intro messages + rules, start
    def intro(self):
        self.line(.5, r=2)
        print("Welcome to Scrambled(tm), a word guessing game.")
        self.line(.5, "You'll have 3 tries to guess the scrambled word.")
        print("If you succeed, you'll move on to the next level.")
        print("If you fail, game over!!!")
        print("Win 5 rounds, and you're the chapmion.")
        self.line(.5, '')
        print("Enter 'quit' at any time to stop playing.")
        self.line(.5, '')
        print("Let's get started...")
        self.line(.5)

        self.start()

    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, diff):
        if diff == "easy":
            self._difficulty = 7
        elif diff == "med":
            self._difficulty = 8
        elif diff == "hard":
            self._difficulty = 9
        else:
            print("Couldn't set difficulty...")

    @property
    def high_score(self):
        return self._high_score

    @high_score.setter
    def high_score(self, score):
        self._high_score = score

    #   Scramble letters
    def scramble(self, word_list):
        #   Create a new list from scrambled words from og list
        joiner = ''
        _scrambled = [joiner.join(random.sample(word, len(word))) for word in word_list]
        #   Return scrambled list
        return _scrambled

    #   Countdown in seconds
    def countdown(self, s):
        self.line(1, r=2)
        _time = int(s)
        _clock = "Game starts in... {}"
        while _time > 0:
            time.sleep(1)
            print(_clock.format(_time))
            
            _time -= 1

    #   Draw scrambled word and discard from list
    def draw_from_top(self, words):
        new_word = words.pop()
        return new_word

    #   Ask to restart
    def ask_to_restart(self):
        while True:
            self.line(.5)
            cmd = input("Want to play again? (y/n): ").lower().strip()
            if "no" in cmd or "n" in cmd:
                self.line(.5)
                print("Guess you've had enough...")
                return False
            elif "yes" in cmd or "y" in cmd:
                self.line(.5)
                print("Alright! New game coming right up...")
                return True
            else:
                print("Oops! I didn't catch that...")

    #   Game script
    def play_game(self):

        diff = self.difficulty
        diff_mod = diff - 7

        #   Random list of words from vocab, descending from 8chars, depending on diff
        wordList1 = [self.vocab.get_rand_word('x', 'z', nchar=diff-n) for n in range(5)]
        #   Scrambled list of words
        wordList2 = self.scramble(wordList1)

        #   PREVIEW WORDS
        #self.line(.5, f"Your words: {wordList1}")

        #   Countdown 3 seconds
        self.countdown(3)

        #   Start Playing
        score = int(0)
        lost = False

        #   Level(i)
        for l in range(5):
            #   Exit if player lost
            if lost:
                break
            #   Otherwise, proceed to level
            self.line(1, r=2)
            print(f"Level {l + 1}")
            if l == 4:
                print("Final round!")
            self.line(.5, '')
            word = self.draw_from_top(wordList2)
            print(f"Word:    {word}")

            #   Try(j)
            for t in range(3):
                self.line(.5)
                #   Get a guess
                guess = input(f"Guess {t + 1}: ").lower().strip()
                #   Check for quit command
                if guess == 'quit':
                    #   If user enters 'quit', lose
                    lost = True
                    break

                #   Check quess
                goal: str = wordList1[-(l + 1)]
                is_correct: bool = (guess == goal)
                self.line(.5, '')
                if is_correct:
                    #   If correct, output message, add score, next level
                    self.line(.5, random.choice(self.correct_messages).format(t + 1))
                    #   Score is (max tries) minus (current try), plus diff modifier
                    score += ((3 - t) + diff_mod)
                    self.line(.5, f"Score: {score}")
                    break
                if not is_correct and t != 2:
                    #   If incorrect and tries remaining, hint and guess again
                    self.line(.5, random.choice(self.wrong_messages))
                    if t == 0:
                        self.line(.5, "Here's a hint: The first letter is '{}'".format(goal[0]))
                    if t == 1:
                        self.line(.5, "Here's a hint: The last letter is '{}'".format(goal[-1]))
                elif not is_correct and t == 2:
                    #   If incorrect and final try, lose
                    self.line(.5, "Oh no! You're out of tries...")
                    self.line(.5, f"The correct answer was : '{goal}'")
                    lost = True
                    break

        #   Game Over
        #   If player lost, print random lose message
        if lost:
            self.line(2, r=2)
            print("YOU LOSE")
            print(f"Score:    {score}")
            self.line(r=2)
            self.line(1, random.choice(self.lose_messages))
            return score

        #   If player won, print random win message
        if not lost:
            self.line(2, r=2)
            print("YOU WIN")
            print(f"Score:    {score}")
            self.line(r=2)
            self.line(1, random.choice(self.win_messages))
            return score


    def bye(self):
        self.line(1, '')
        print("See you later!")
        self.line()


    def start(self):
        playing = True
        while playing:
            #   Set difficulty
            while True:
                diff = input("Difficulty (easy, med, hard): ").strip().lower()
                if "easy" in diff or "med" in diff or "hard" in diff:
                    break
                print("Didn't catch that...")
            self.difficulty = diff
            print("Difficulty set.")
            #   Play game, get score
            game_score = self.play_game()
            #   Record if new high score
            if game_score > self.high_score:
                self.high_score = game_score
                self.line(.5)
                print(f"New high score:    {self.high_score}")
            #   Ask to play again
            playing = self.ask_to_restart()
        #   Say bye
        self.bye()

