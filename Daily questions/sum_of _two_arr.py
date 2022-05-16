def sum_arr(arr1, arr2):
    sum_list = []
    for i in range(0, len(arr1)):
        sum_list.append(arr1[i] + arr2[i])
    return sum_list


if __name__ == '__main__':
    arr_1 = [1, 2]
    print("The first array is", arr_1)
    arr_2 = [2, 4]
    print("The second array is", arr_2)
    output = sum_arr(arr_1, arr_2)
    print("The sum of the elements in the arrays are", output)