# Jaziel Lopez <juan.jaziel@gmail.com>
# Software Developer
# http://jlopez.mx

import time


def sort(needle, output, haystack):

    """
    Alphabetic sort

    :param needle:
    :param output:
    :param haystack:
    :return: tmp
    """

    tmp = []

    for i in range(0, len(output)):

        previous = output[i]

        if needle == previous:

            e = Exception("{0} is duplicated in \n \"{1}\"".format(needle, haystack))

            raise Exception(e)

        if needle < previous:

            cloned = output[i:len(output)]

            tmp.append(needle)

            for clone in cloned:

                tmp.append(clone)

            return tmp

        else:

            tmp.append(previous)

    tmp.append(needle)

    return tmp

haystack = "On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and " \
           "demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee " \
           "the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty " \
           "through weakness of will, which is the same as saying through shrinking from toil and pain. " \
           "These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is " \
           "untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be " \
           "welcomed and every pain avoided." \
           "But in certain circumstances and owing to the claims of duty or the obligations of business it will " \
           "frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore " \
           "always holds in these matters to this principle of selection: he rejects pleasures to secure other " \
           "greater pleasures, or else he endures pains to avoid worse pains."

start = time.time()

try:

    output = []

    for current in range(0, len(haystack)):

        needle = haystack[current]

        if needle == ' ':

            continue

        if current == 0:

            output.append(needle)

            continue

        output = sort(needle, output, haystack)

    print('"{0}" has unique characters'.format(haystack))

except Exception as e:

    print(e)

finally:

    print("--- %s seconds ---" % (time.time() - start))

    print('Done')
