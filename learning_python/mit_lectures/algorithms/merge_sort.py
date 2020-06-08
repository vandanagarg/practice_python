''' merge sort algorithm - nlog(n) Complexity; where n is len(L)
Much faster then all other sorting algorithms
Divide and Conquer rule to first divide the list into 2 half's to
smallest pieces and then merge the sorted lists together '''


# merging sublists step
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
    print("merge: " + str(left) + " & " + str(right))
    print("result " + str(result))
    return result


# merge sort algorithm - recursive
def merge_sort(L):
    print("merge sort:" + str(L))
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
    return merge(left, right)


test_list = [1, 3, 5, 7, 2, 6, 25, 18, 13]

print("sorted list:" + str(merge_sort(test_list)))
print(test_list)
