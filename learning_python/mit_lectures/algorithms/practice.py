# bogo sort
import random


def is_sorted(L):
    if sorted(L) == L:
        return True
    else:
        return False


def bogo_sort(L):
    while not is_sorted(L):
        print(L)
        random.shuffle(L)
    return L


# L = [2, 3, 1]
# L = [1, 2, 3]
# print(bogo_sort(L))


# bubble sort
def bubble_sort(L):
    swap = False
    while not swap:
        print("mid " + str(L))
        swap = True
        for i in range(1, len(L)):
            if L[i-1] > L[i]:
                swap = False
                L[i-1], L[i] = L[i], L[i-1]
    return L


# L = [2, 3, 1]
# print(bubble_sort(L))

# selection sort
def selection_sort(L):
    start_point = 0
    while start_point != len(L):
        print("mid " + str(L))
        for i in range(start_point, len(L)):
            # print(L)
            if L[start_point] > L[i]:
                L[start_point], L[i] = L[i], L[start_point]
        start_point += 1
    return L


# L = [4, 2, 3, 1]
# print(selection_sort(L))

# merge sort

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result


def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        mid = len(L)//2
        left = merge_sort(L[:mid])
        right = merge_sort(L[mid:])
    return merge(left, right)


L = [4, 2, 3, 1]
print(merge_sort(L))
