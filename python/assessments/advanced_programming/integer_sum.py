# https://www.programmingexpert.io/advanced-programming/assessment/2

def flatten_lists(func):
    def wrapper(*args, **kwargs):
        new_args = []
        for arg in args:
            if type(arg) == list:
                for elem in arg:
                    new_args.append(elem)
            else:
                new_args.append(arg)

        result = func(*new_args, **kwargs)
        return result

    return wrapper

def convert_strings_to_ints(func):
    def wrapper(*args, **kwargs):
        new_args = []
        for arg in args:
            if type(arg) == str:
                if arg.isnumeric():
                    new_args.append(int(arg))
            else:
                new_args.append(arg)

        result = func(*new_args, **kwargs)
        return result

    return wrapper

def filter_integers(func):
    def wrapper(*args, **kwargs):
        new_args = []
        for arg in args:
            if type(arg) == int:
                new_args.append(arg)

        result = func(*new_args, **kwargs)
        return result

    return wrapper

@flatten_lists
@convert_strings_to_ints
@filter_integers
def integer_sum(*args):
    return sum(args)

args = ["1", "2", -0.9, 4, [5, "hi", "3"]]

print(integer_sum(*args))