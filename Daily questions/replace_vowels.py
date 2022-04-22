def replace_vowels(test_str, R):

    new_string = ""
    for i in range(len(str)):
        if str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u':
            new_string = new_string + R
        else:
            new_string = new_string + str[i]


if __name__ == "__main__":
    input_str = "how are you?"

    # specified character
    m = "mm"

    # printing input
    print("Given String:", input_str)
    print("Given Specified Character:", m)

    # printing output
    print("After replacing vowels with the specified character:",
          replace_vowels(input_str, m))
