''' Given the participants' score sheet for your University
Sports Day, you are required to find the runner-up score.
You are given n scores. Store them in a list and find the
score of the runner-up.
# sample input
5
2 3 6 6 5
# o/p 5
'''

n = int(input())
arr = map(int, input().split())


new_list = list(reversed(sorted(arr)))
for i in range(1, len(new_list)):
    if new_list[i-1] == new_list[i]:
        continue
    else:
        print(new_list[i])
        break
