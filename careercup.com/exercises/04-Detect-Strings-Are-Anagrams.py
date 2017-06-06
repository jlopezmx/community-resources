# Jaziel Lopez <juan.jaziel@gmail.com>
# Software Developer
# http://jlopez.mx

words = {'left': "secured", 'right': "rescued"}


def anagram(left="", right=""):

    """
    Compare left and right strings
    Determine if strings are anagram
    :param left:
    :param right:
    :return:
    """

    # anagram: left and right strings have been reduced to empty strings
    if not len(left) and not len(right):

        print("Anagram!")

        return True

    # anagram not possible on asymetric strings
    if not len(left) == len(right):

        print("Impossible Anagram: asymetric strings `{}`({}) - `{}`({})".format(left, len(left), right, len(right)))

        return False

    # get first char from left string
    # it should exist on right regardless char position
    # if first char from left does not exist at all in right string
    # anagram is not possible
    char = left[0]

    if not has_char(right, char):

        print("Impossible Anagram: char `{}` in `{}` not exists in `{}`".format(char, left, right))

        return False

    left = reduce(left, char)

    right = reduce(right, char)

    if len(left) and len(right):

        print("After eliminating char `{}`\n `{}` - `{}`\n".format(char, left, right))

    else:

        print("Both strings have been reduced\n")

    # keep reducing left and right strings until empty strings
    # anagram is possible when left and right strings are reduced to empty strings
    anagram(left, right)


def has_char(haystack, char):

    """
    Determine if a given char exists in a string regardless of the position
    :param haystack:
    :param char:
    :return:
    """

    char_in_string = False

    for i in range(0, len(haystack)):

        if haystack[i] == char:

            char_in_string = True

            break

    return char_in_string


def reduce(haystack, char):

    """
    Return a reduced string after eliminating `char` from original haystack
    :param haystack:
    :param char:
    :return:
    """

    output = ""

    char_times_string = 0

    for i in range(0, len(haystack)):

        if haystack[i] == char:

            char_times_string += 1

        if haystack[i] == char and char_times_string > 1:

            output += haystack[i]

        if haystack[i] != char:

            output += haystack[i]

    return output


print("\nAre `{}` and `{}` anagrams?\n".format(words['left'], words['right']))

anagram(words['left'], words['right'])


# How to use:
# $ python3 04-Detect-Strings-Are-Anagrams.py
# 
#  Are `secured` and `rescued` anagrams?
#
# After eliminating char `s`
# `ecured` - `recued`
#
# After eliminating char `e`
# `cured` - `rcued`
#
# After eliminating char `c`
# `ured` - `rued`
#
# After eliminating char `u`
# `red` - `red`
#
# After eliminating char `r`
# `ed` - `ed`
#
# After eliminating char `e`
# `d` - `d`
#
# Both strings have been reduced
#
# Anagram!
#
# Process finished with exit code 0
