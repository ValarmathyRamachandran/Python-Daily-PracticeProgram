# Python3 program to print
# even length words in a string

def print_words(s):
    # split the string
    s = s.split(' ')
    print(s)

    # iterate in words of string
    for word in s:

        # if length is even
        if len(word) % 2 == 0:
            print(word)


if __name__ == "__main__":
    s = "i am Valarmathy"
    print_words(s)

