# replace a string

string = "abracadabra"
l = list(string)  # noqa:E741
l[5] = 'k'
print(l)
string = ''.join(l)
print(string)
# abrackdabra

# Find a string

string = "ABCDCDCDC"
sub_string = "CDC"


def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count


print(count_substring(string, sub_string))
