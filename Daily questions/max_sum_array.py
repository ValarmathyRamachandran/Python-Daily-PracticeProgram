def max_subarray(inp):
    max_sum = inp[0]
    current_sum = inp[0]
    for i in range(1, len(inp) - 1):
        current_sum += inp[i]
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum


if __name__ == "__main__":
    a = [1, 2, -2, 4]
    # a= [1, -5, -4, -1, 6, 3, -9]
    print(max_subarray(a))
