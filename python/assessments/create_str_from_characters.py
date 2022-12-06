# https://www.programmingexpert.io/programming-fundamentals/assessment/6

def count_characters_in_str(string):
    str_characters = {}
    for char in string:
        str_characters[char] = str_characters.get(char, 0) + 1

    return str_characters


def merge_characters_count(array):
    dict1, dict2 = array[0], array[1]
    combined_chars = dict1.copy()
    for char, freq in dict2.items():
        combined_chars[char] = combined_chars.get(char, 0) + freq

    return combined_chars


# Version 2
def create_strings_from_characters(frequencies, string1, string2):
    str1_characters = count_characters_in_str(string1)
    str2_characters = count_characters_in_str(string2)
    str_list = [str1_characters, str2_characters]

    code = 2
    for str_chars in str_list:
        for char, freq in str_chars.items():
            if char in frequencies:
                if freq > frequencies[char]:
                    code -= 1
                    break
            else:
                code -= 1
                break

    if code == 2:
        combined_chars = merge_characters_count(str_list)
        for char, freq in combined_chars.items():
            if char in frequencies:
                if freq > frequencies[char]:
                    code -= 1
                    break
            else:
                code -= 1
                break

    return code


# Version 3 (more compact code)
def create_strings_from_characters(frequencies, string1, string2):
    def check_frequencies(dic, code):
        for char, freq in dic.items():
            if char in frequencies:
                if freq > frequencies[char]:
                    return code - 1
            else:
                return code - 1
        
        return code

    str1_characters = count_characters_in_str(string1)
    str2_characters = count_characters_in_str(string2)
    str_list = [str1_characters, str2_characters]

    code = 2
    for str_chars in str_list:
        code = check_frequencies(str_chars, code)

    if code == 2:
        combined_chars = merge_characters_count(str_list)
        code = check_frequencies(combined_chars, code)

    return code


# First version (unfinished)
# def create_strings_from_characters(frequencies, string1, string2):
#     str1_characters = count_characters_in_str(string1)
#     str2_characters = count_characters_in_str(string2)

#     code = 0
#     str1_sufficient = True
#     for char, freq in str1_characters.items():
#         if char in frequencies:
#             if freq > frequencies[char]:
#                 str1_sufficient = False
#                 break
#         else:
#             str1_sufficient = False
#             break

#     str2_sufficient = True
#     for char, freq in str2_characters.items():
#         if char in frequencies:
#             if freq > frequencies[char]:
#                 str2_sufficient = False
#                 break
#         else:
#             str2_sufficient = False
#             break

#     if str1_sufficient:
#         code += 1
#     if str2_sufficient:
#         code += 1

#     return code

# Does not take into account the possibility to make both strings at once
# only the possibility to do both separately