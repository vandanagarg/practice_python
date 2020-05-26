''' implement binary search '''



num = 390

def check_num(l):
    l_original = l

    len_l = len(l)
    # print(len_l)

    if len_l % 2 == 0:
        mid = len_l//2
        # print(mid)
        # print(l[(mid)-1])
        if num[0] == l[(mid)-1]:
            print("position is {}".format((mid)-1))
        elif num[0] < l[(mid)-1]:
            l = []
            l.append(l_original[: mid])
            check_num(l)  # start recursion
        elif num[0] > l[(mid)-1]:
            l = []
            l.append(l_original[mid:])
            check_num(l)  # start recursion
    else:
        mid = len_l//2
        if num[0] == l[(mid)-1]:
            print("position is {}".format((mid)-1))
        elif num[0] < l[(mid)-1]:
            l = []
            l.append(l_original[: mid])
            check_num(l)  # start recursion
        elif num[0] > l[(mid)-1]:
            l = []
            l.append(l_original[mid:])
            check_num(l)  # start recursion

l = [1, 5, 12, 24, 35, 64, 117, 283, 390, 1000]
check_num(l)
