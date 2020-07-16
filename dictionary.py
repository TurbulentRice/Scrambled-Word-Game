import json
import random

#   Dictionary class, loads JSON into dict 'vocabulary'
class Dictionary:
    def __init__(self, lang: str = "eng", trim=True):
        #   Main dict object
        self.vocabulary: dict = {}
        self.trash: dict = {}

        if "eng" in lang.strip().lower():
            with open("WebstersEnglishDictionary.JSON", "r") as read_data:
                self.vocabulary = dict(json.load(read_data))
        if trim:
            self.trim(" ", "-")

    def trim(self, *exclude):
        #   Delete entries whose key includes " ", "-"
        #   Consider deleting items whose value includes [Obs.],[Archaic],[R.]
        for key, value in self.vocabulary.items():
            for c in exclude:
                if c in key:
                    self.trash[key] = self.vocabulary[key]
                    break
        for key in self.trash.keys():
            if key in self.vocabulary.keys():
                del self.vocabulary[key]

    #   Words in vocab
    def get_size(self):
        return len(self.vocabulary)

    #   Longest word
    def get_longest_word(self):
        return max(self.vocabulary, key=len)

    #   Lookup word definition
    def get_def(self, k: str):
        key = k.strip().lower()
        val = self.vocabulary.get(key, f"Word '{key}' not found!")
        return val

    #   Return random word that meets criteria (excluded chars, num chars)
    #   DEFAULT returns one random word of any length
    def get_rand_word(self, *exclude, nchar: int = 0, r_val=False):
        pick, val = random.choice(list(self.vocabulary.items()))
        has_badchar = False
        good_length = True
        #   Check for excluded char
        for letter in exclude:
            if letter in pick:
                has_badchar = True
                break
        #   Check length only if nchar set
        if (nchar > 0) and (len(pick) != nchar):
            good_length = False

        #   Check for criteria
        if (has_badchar is False) and (good_length is True):
            if r_val:
                return pick, val    #   Returns 2 strings
            elif not r_val:
                return pick         #   Returns only word
        #   Otherwise try new rand word
        else:
            return self.get_rand_word(*exclude, nchar=nchar, r_val=r_val)



