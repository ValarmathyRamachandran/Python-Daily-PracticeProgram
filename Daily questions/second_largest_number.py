# Python program to find second largest
# number in a list

list1 = [10, 20, 4, 45, 99]

mx = max(list1[0], list1[1])
secondmax = min(list1[0], list1[1])
n = len(list1)
for i in range(2, n):
    if list1[i] > mx:
        secondmax = mx
        mx = list1[i]
    elif secondmax < list1[i] != mx:
        secondmax = list1[i]

print("Second highest number is : ", str(secondmax))
