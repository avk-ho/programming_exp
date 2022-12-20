# https://www.programmingexpert.io/advanced-programming/assessment/4

from threading import Lock

class WordCounter:
    def __init__(self):
        self.words = {}
        self.lock = Lock()

    def process_text(self, text):
        words = text.split(" ")
        self.lock.acquire()
        for word in words:
            self.words[word] = self.words.get(word, 0) + 1

        self.lock.release()


    def get_word_count(self, word):
        return self.words.get(word, 0)
