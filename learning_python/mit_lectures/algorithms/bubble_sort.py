''' Bubble sort - Quadratic complexity
Here we get pass through in atmost n times
where b is length of the list '''


def bubble_sort(L):
    swap = False
    while not swap:
        print("bubble sort: " + str(L))
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp


test_list = [1, 3, 5, 7, 2, 6, 25, 18, 13]

bubble_sort(test_list)
print(test_list)
