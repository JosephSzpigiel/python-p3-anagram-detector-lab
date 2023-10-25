# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word  = word

    def match(self, word_list):
        result = []
        for w in word_list:
            if sorted(list(self.word)) == sorted(list(w)):
                result.append(w)
        return result