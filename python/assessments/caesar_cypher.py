# https://www.programmingexpert.io/programming-fundamentals/assessment/2

# simplified version of the caesar cypher
# 0 <= offset <= 26
# characters are offset to the "left", "tim" with offset 2 becomes "rgk"
# string will always contain only lowercase letters

def caesar_cipher(string, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = list(alphabet)
    # print(string)
    encoded_string = ""
    for letter in string:
        idx = alphabet.index(letter)
        offset_idx = (idx - offset) % 26
        encoded_string += alphabet[offset_idx]

    # print(encoded_string)
    return encoded_string
