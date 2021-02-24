"""
http://adilet.org/blog/palindromic-tree/
"""


def pal_tree():
    pass


"""
Basic (find only distinct palindromes)
"""


def find_palindromes_in_sub_string(str, j, k):
    count = 0
    while j >= 0 and k < len(str):
        if str[j] != str[k]:
            break
        print(str[j: k + 1])
        count += 1

        j -= 1
        k += 1

    return count


def find_all_palindrome_substrings(str):
    count = 0
    for i in range(0, len(str)):
        count += find_palindromes_in_sub_string(str, i - 1, i + 1)
        count += find_palindromes_in_sub_string(str, i, i + 1)

    return count


"""
Naive and Trivial
"""


def countSubstrings(s):
    counter = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            temp = s[i:j]
            if temp == temp[::-1]:
                print(temp)
                counter += 1
    return counter


"""
Manacker
"""


# Find palindromes like 2*N
# See PalN2.
# P.S. About magic numbers : you can read about this in the description of the algorithm of Manacker.
# These numbers need for finding palindromes like 2*N because not allowed to find centre of these palindrome
def pal2(str, ansPal2):
    leftBorder = 0
    rightBorder = -1
    tempMirror = 0

    for i in range(len(str)):
        if i > rightBorder:
            tempMirror = 0
        else:
            tempMirror = min(ansPal2[leftBorder + rightBorder - i + 1], rightBorder - i + 1)

        while i + tempMirror < len(str) and i - tempMirror - 1 >= 0 and str[i + tempMirror] == str[i - tempMirror - 1]:
            tempMirror += 1
        ansPal2[i] = tempMirror
        if i + tempMirror - 1 > rightBorder:
            leftBorder = i - tempMirror
            rightBorder = i + tempMirror - 1


# Find palindromes like 2*N+1
def palN2(str, ansPalN2):
    leftBorder = 0
    rightBorder = -1
    tempMirror = 0
    for i in range(len(str)):
        if i > rightBorder:
            tempMirror = 1
        else:
            tempMirror = min(ansPalN2[leftBorder + rightBorder - i], rightBorder - i)

        while i - tempMirror >= 0 and i + tempMirror < len(str) and str[i - tempMirror] == str[i + tempMirror]:
            tempMirror += 1

        ansPalN2[i] = tempMirror

        if i + tempMirror - 1 > rightBorder:
            leftBorder = i - tempMirror + 1
            rightBorder = i + tempMirror - 1


def find_all(s):
    ansPal2 = [0] * len(s)
    ansPalN2 = [0] * len(s)

    pal2(s, ansPal2)
    palN2(s, ansPalN2)

    print(ansPal2)
    print(ansPalN2)
    count = 0
    for k in range(len(s)):
        count += (ansPal2[k] + ansPalN2[k])

    return count


"""
Choose wisely
"""

print(find_all_palindrome_substrings('radar'))
