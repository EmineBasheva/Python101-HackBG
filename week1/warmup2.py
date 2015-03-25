from warmup import sum_of_digits


# === 1 ===
def sum_of_divisors(n):
    if n < 0:
        n *= -1
    else:
        return sum([i for i in range(1, n + 1) if n % i == 0])


# === 2 ===
def is_prime(n):
    return sum_of_divisors(n) == n + 1


# === 3 ===
def prime_number_of_divisors(n):
    return is_prime(len([i for i in range(1, n + 1) if n % i == 0]))


# === 4 ===
def contains_digit(number, digit):
    number = str(number)
    digit = str(digit)

    return digit in number


# === 5 ===
def contains_digits(number, digits):
    number = str(number)
    for digit in digits:
        if str(digit) not in number:
            return False

    return True


# === 6 ===
def is_number_balanced(n):
    n = str(n)
    middle = len(n) // 2
    left = n[:middle]

    if len(n) % 2 == 0:
        right = n[middle:]
    else:
        right = n[middle + 1:]

    return sum_of_digits(right) == sum_of_digits(left)


# === 7 ===
def count_substrings(haystack, needle):
    return haystack.count(needle)


# === 8 ===
def zero_insert(n):
    n = str(n)
    result = n[0]

    for x in range(1, len(n)):
        if (n[x - 1] == n[x]) or ((int(n[x - 1]) + int(n[x])) % 10 == 0):
            result = result + '0' + n[x]
        else:
            result = result + n[x]

    return int(result)  # stupid


# === 9 ===
def sum_matrix(m):
    return sum([sum(row) for row in m])


# === 10 ===
def all_elements(m):
    elements = [(m.index(new_m), new_m.index(elem
                                             )) for new_m in
                m for elem in new_m]
    return {elem: m[elem[0]][elem[1]] for elem in elements}


def find_neighbours(m, elem):
    elements = all_elements(m)

    result = [some_elem for some_elem in elements
              if some_elem[0] in range(elem[0] - 1, elem[0] + 2) and
              some_elem[1] in range(elem[1] - 1, elem[1] + 2)]
    del result[result.index(elem)]
    return result

# def matrix_bombing_plan(m):


print(find_neighbours([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], (1, 0)))
