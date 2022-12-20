# https://www.programmingexpert.io/advanced-programming/assessment/1

# must use map, filter, lambda

def positive_even_squares(*args):
    even_positives = []
    for lst in args:
        # print(lst)
        filtered_lst = list(filter(lambda x: x % 2 == 0 and x > 0, lst))
        even_positives.append(filtered_lst)

    squared_even_positives = []
    for lst in even_positives:
        # print(lst)
        squared_lst = list(map(lambda x: x**2, lst))
        squared_even_positives.extend(squared_lst)

    return squared_even_positives

args = [[-5, 2, 3, 4, 5], [1, 3, 5, 6, 7], [-9, -8, 10]]

print(positive_even_squares(*args))