''' Lists and executing its commands '''

if __name__ == '__main__':
    n = 4
    l2 = []
    for _ in range(n):
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if cmd != "print":
            cmd += "(" + ",".join(args) + ")"
            eval("l2."+cmd)
        else:
            print(l2)


'''
insert 0 6
insert 1 5
remove 6
print
'''
