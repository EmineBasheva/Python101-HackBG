from warmup import to_digits
from warmup import to_number
from warmup2 import is_prime
from datetime import date


# === 1 ===
def count_words(arr):
    return {word: arr.count(word) for word in arr}


# === 2 ===
def unique_words_count(arr):
    return len(set(arr))


# === 3 ===
def nan_expand(times):
    if times == 0:
        return ""
    return str(times * "Not a " + "NaN")


# === 4 ===
def iterations_of_nan_expand(expanded):
    if all(nan_expand(i) in expanded
           for i in range(0, expanded.count("Not a"))):
        return expanded.count("Not a")
    return False
    # if "NaN" in expanded:
    #     return expanded.count("Not a")
    # elif expanded == "":
    #     return 0
    # return False


# === 5 ===
def prime_factorization(n):
    result = []

    for index in range(2, n + 1):
        count = 0
        while n % index == 0:
            count += 1
            n /= index
        if not(count == 0):
            result.append((index, count))
    return result


# === 6 ===
def take_same(things):
    result = []
    index = 0

    if things == []:
        return []

    if index == len(things) - 1:
        return [things[index]]

    while things[index] == things[index + 1] and index < len(things) - 2:
        result.append(things[index])
        index += 1
    if index == len(things) - 2:
        result.append(things[index])
        index += 1
    result.append(things[index])
    return result


def group(things):
    result = []

    while not (things == []):
        result.append(take_same(things))
        things = things[len(take_same(things)):]

    return result


# === 7 ===
def max_consecutive(items):
    group_items = group(items)
    max_count = 0

    for item in group_items:
        if max_count < len(item):
            max_count = len(item)

    return max_count


# === 8 ===
def groupby(func, seq):
    result = {}

    for item in seq:
        if func(item) not in result:
            result[func(item)] = []

        result[func(item)].append(item)

    return result


# === 9 ===
def prepare_meal(number):
    result = ""
    n = 1
    last_n = 0

    while n < number:
        if number % (3 ** n) == 0:
            last_n = n
        n += 1

    result = ("spam " * last_n)[:-1]

    if number % 5 == 0:
        if result == "":
            return "eggs"
        return result + " and eggs"
    return result


# === 10 ===
def reduce_file_path(path):
    parts = path.split("/")
    items = []

    for part in parts:
        if not(part == "" or part == "."):
            items.append(part)

    elements = []
    for i in range(0, len(items) - 1):
        if not(items[i + 1] == ".." or items[i] == ".."):
            elements.append(items[i])

    if items == []:
        return "/"

    if not(items[len(items) - 1] == ".."):
        elements.append(items[len(items) - 1])

    return "/" + "/".join(elements)


# === 11 ===
def is_an_bn(word):
    if len(word) % 2 == 1:
        return False
    n = len(word) / 2
    my_word = ("a" * n) + ("b" * n)

    if my_word == word:
        return True
    return False


# === 12 ===
def is_credit_card_valid(number):
    if number % 2 == 0:
        return False
    number_to_digits = to_digits(number)

    for index in range(0, len(number_to_digits)):
        if index % 2 == 1:
            number_to_digits[index] *= 2

    new_number = to_number(number_to_digits)
    sum_of_digits = sum(to_digits(new_number))

    return sum_of_digits % 10 == 0


# === 13 ===
def goldbach(n):
    result = []

    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            result.append((i, n - i))

    return result


# === 14 ===
def magic_square(matrix):
    n = len(matrix[0])
    sum_row = sum(matrix[0])
    sum_column = sum([elem[0] for elem in matrix])
    sum_forward_d = sum([matrix[i][i] for i in range(0, n)])
    sum_backward_d = sum([matrix[i][n - i - 1] for i in range(0, n)])

    are_magic_rows = all(sum(matrix[i]) == sum_row for i in range(0, n))
    are_magic_columns = all(
        sum([elem[i] for elem in matrix]) for i in range(0, n))
    are_magic_first = sum_row == sum_column == sum_forward_d == sum_backward_d

    return are_magic_rows and are_magic_columns and are_magic_first


# === 15 ===
# def fridays_in_year(year):
#     first_date = date(year, 1, 1)
#     last_date = date(year, 12, 31)
#     all_days = (last_date - first_date).days

#     if all_days == 365:
#         return 53

#     return 52

def is_leap_year(year):
    if year % 400 == 0:
        # print("400")
        return True
    if year % 100 == 0:
        # print("100")
        return False
    if year % 4 == 0:
        # print("4")
        return True
    return False


def friday_years(start, end):
    count_fridays = 0

    for year in range(start, end + 1):
        if is_leap_year(year):
            count_fridays += 1

    return count_fridays
    # return sum([1 for year in range(start, end + 1)
    #             if fridays_in_year(year) == 53])


print(friday_years(1000, 2000))
