# all(), any()


n = input()
input_list = input().split(" ")
print(all
      ([
        all([int(i) > 0 for i in input_list]),
        any([i == i[::-1] for i in input_list])
        ]))

# n = input()
# s = map(int, input().split())
# print(s)
# print([False, any(map(lambda x: str(x) == str(x)[::-1], s))
#        ][all(map(lambda x: x > 0, s))])


# 6
# 1 2 3 4 5 -9
# ans: False
