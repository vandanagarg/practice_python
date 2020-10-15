''' Task is to wrap the string into a paragraph of width '''
import textwrap


def wrap(string, max_width):
    p = textwrap.wrap(string, width=max_width)
    return "\n".join(p)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# or
# def wrap2(string, max_width):
#     return "\n".join([string[i:i+max_width] for i in range(
#       0, len(string), max_width)])


string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width = 4

print([string[i:i+max_width] for i in range(0, len(string), max_width)])
