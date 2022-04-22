def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    if a_set & b_set:
        return a_set & b_set
    else:
        return "No common elements"


if __name__ == "__main__":
    a = [1, 3, 5, 9]
    b = [4, 5, 6, 9]
    print(common_member(a, b))
