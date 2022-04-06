# generate random strings

import random
import string


def random_str(length_inp):
    """
    :param length_inp: Length of the string which we need to randomly generate
    :return: No of times it takes to generate our desired string
    """
    result = ""
    count = 0
    while result != "hel":
        result = ''.join((random.choice(string.ascii_lowercase) for x in range(length_inp)))
        print(" Random string generated: ", result)
        count += 1
    return count


if __name__ == "__main__":
    length = 3
    print("Count : {}".format(random_str(length)))
