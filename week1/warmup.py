# === 1 ===
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# === 2 ===


def fibonacci(n):
    result = []
    for x in xrange(0, n):
        if x == 0 or x == 1:
            result.append(1)
        else:
            result.append(result[x - 1] + result[x - 2])
    return result


# === 3 ===
def sum_of_digits(n):
    if n < 0:
        n *= -1
    n = str(n)

    sum_all = 0
    for i in range(0, len(n)):
        sum_all += int(n[i])

    return sum_all


# === 4 ===
def fact_digits(n):
    n = str(n)

    sum_all_fact = 0
    for i in range(0, len(n)):
        sum_all_fact += factorial(int(n[i]))

    return sum_all_fact


# === 5 ===
def palindrome(obj):
    obj = str(obj)
    for x in xrange(0, len(obj) // 2):
        if obj[x] != obj[len(obj) - x - 1]:
            return False
    return True


# === 6 ===
def to_digits(n):
    digits_all = []
    n = str(n)
    for x in xrange(0, len(n)):
        digits_all.append(int(n[x]))
    return digits_all


# === 7 ===
def to_number(digits):
    result = ""
    for i in range(0, len(digits)):
        result += str(digits[i])

    return int(result)


# === 8 ===
def fib_number(n):
    return to_number(fibonacci(n))


# === 9 ===
def count_vowels(string):
    string = string.lower()
    vowels = "aeiouy"
    count = 0

    for letter in string:
        for vowel in vowels:
            if letter == vowel:
                count += 1

    return count


# === 10 ===
def count_consonants(string):
    string = string.lower()
    consonants = "bcdfghjklmnpqrstvwxz"
    count = 0

    for letter in string:
        for consonant in consonants:
            if letter == consonant:
                count += 1

    return count


# === 11 ===
def char_histogram(string):
    result = {}
    for letter in string:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1

    return result


# === 12 ===
def p_score(n):
    if palindrome(n):
        return 1
    return 1 + p_score(n + int(str(n)[::-1]))


# === 13 ===
def is_increasing(seq):
    for i in range(0, len(seq) - 1):
        if seq[i] >= seq[i + 1]:
            return False
    return True


# === 14 ===
def is_decreasing(seq):
    for i in range(0, len(seq) - 1):
        if seq[i] <= seq[i + 1]:
            return False
    return True


# === 15 ===
def is_hack_number(number):
    binary_number = "{0:b}".format(number)
    count_one = 0

    for number in binary_number:
        if number == '1':
            count_one += 1

    if palindrome(binary_number) and count_one % 2 == 1:
        return True
    return False


def next_hack(n):
    n += 1
    while not(is_hack_number(n)):
        n += 1
    return n


# print(next_hack(8031))
