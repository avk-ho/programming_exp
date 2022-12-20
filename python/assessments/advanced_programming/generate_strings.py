# https://www.programmingexpert.io/advanced-programming/assessment/3

# frequency always >= 0

def generate_string(string, frequency):
    for char in string:
        for i in range(frequency):
            yield char


class GenerateString:
    def __init__(self, string, frequency):
        self.string = string
        self.frequency = frequency     

    def __iter__(self):
        self.current_char_idx = 0
        self.count = 0
        return self

    def __next__(self):
        self.count += 1

        if self.count > self.frequency:
            self.current_char_idx += 1
            self.count = 1

        if self.current_char_idx >= len(self.string):
            raise StopIteration
        else:
            return self.string[self.current_char_idx]
        