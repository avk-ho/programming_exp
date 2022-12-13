# https://www.programmingexpert.io/programming-fundamentals/assessment/4

def get_n_longest_unique_words(words, n):
    # print(words)
    # print(n)
    valid_words = []
    for word in words:
        if words.count(word) > 1: #O(len(words))T
            continue
    
        sortByLength(valid_words, word)

    # print(valid_words)
    longest_words = []
    while n > 0:
        n -= 1
        longest_word = valid_words.pop()
        longest_words.append(longest_word)

    return longest_words
        

def sortByLength(lst, word):
    if len(lst) == 0:
        lst.append(word)
        return
    
    longest_word = lst.pop()

    if len(word) >= len(longest_word):
        lst.append(longest_word)
        lst.append(word)
    else:
        sortByLength(lst, word)
        lst.append(longest_word)

# in operator is also O(n)T