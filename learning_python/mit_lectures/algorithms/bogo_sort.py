''' Bogo Sort (Type 1) also called as permutation sort
as we can search through all possible permutations '''
import random


def is_sorted(L):
    if sorted(L) == L:
        return True
    else:
        return False


def bogo_sort(L):
    ''' Crisp definition for bogo sort/ permutation sort
        best case: O(n) where n is len(L) and list is sorted
        worst case: O(?): ;is unbounded and could go for ever
        let is_sorted() be a function to check if list is sorted '''
    while not is_sorted(L):
        print(L)
        random.shuffle(L)
    return L


L = [3, 2, 1]
# L = [1, 2, 3]
print(bogo_sort(L))
