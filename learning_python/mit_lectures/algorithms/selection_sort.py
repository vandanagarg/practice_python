''' Selection Sort - Quadratic complexity
A simple sorting way where we find smallest element;
keep it in front and then interchange/flip the places of those 2 numbers
smallest number and number at first position '''


def selection_sort(L):
    suffix_st = 0
    while suffix_st != len(L):
        print("Selection Sort: " + str(L))
        for i in range(suffix_st, len(L)):
            if L[i] < L[suffix_st]:
                L[suffix_st], L[i] = L[i], L[suffix_st]
        suffix_st += 1


test_list = [1, 3, 5, 7, 2, 6, 25, 18, 13]

selection_sort(test_list)
print(test_list)
