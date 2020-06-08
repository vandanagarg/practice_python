''' Linear Search on Sorted List '''


def linear_sorted_search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


L = [4, 10, 15, 20, 45, 48]
print(linear_sorted_search(L, 10))

L_str = ["at", "bat", "fat", "cat", "mat", "rat"]
print(linear_sorted_search(L_str, "cat"))
