# Jaziel Lopez <juan.jaziel@gmail.com>
# Software Developer
# http://jlopez.mx


def reverse(haystack):

    """
    Reverse a C-style string
    (C-String means that 'abcd' is represented as five characters, including the null character.)
    :param haystack:
    :return:
    """

    output = ""

    is_char = len(haystack) - 1

    while is_char:

        is_char -= 1

        output += haystack[is_char]

    return output

sentence = "On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and " \
           "demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee " \
           "the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty " \
           "through weakness of will, which is the same as saying through shrinking from toil and pain.\n"

print(reverse(sentence))

# How to use:
#
# $ python3 02-Reverse-C-style-String.py
#
# .niap dna liot morf gniknirhs hguorht gniyas sa emas eht si hcihw ,lliw fo ssenkaew hguorht ytud rieht ni liaf ohw esoht ot sgnoleb emalb lauqe dna ;eusne ot dnuob era taht elbuort dna niap eht eeserof tonnac yeht taht ,erised yb dednilb os ,tnemom eht fo erusaelp fo smrahc eht yb dezilaromed dna deliugeb os era ohw nem ekilsid dna noitangidni suoethgir htiw ecnuoned ew ,dnah rehto eht nO
#
# Process finished with exit code 0
