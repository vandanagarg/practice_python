#example error handling

try:
    f= open("test_file.txt")
    var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

#
# #o/p:
# # [Errno 2] No such file or directory: 'test_file.txt'
# #name 'bad_var' is not defined
