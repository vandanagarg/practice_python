''' Linear Search on Unsorted List '''


def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found


L = ["Vandana", "Girl", 3, "a"]
print(linear_search(L, "a"))
