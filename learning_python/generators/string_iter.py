#3 string to iterator


s = "hello_miss"

s_iter = iter(s)
print(s_iter)
# print(list(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))   # should generate error StopIteration


