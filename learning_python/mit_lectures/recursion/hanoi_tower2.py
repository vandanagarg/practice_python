''' Tower of Hanoi -
Implementing the famous recursion problem as explained in
[link](https://www.youtube.com/watch?v=buWXDMbY3Ww)
Must also try implementing using arrays and [link]
(https://www.geeksforgeeks.org/python-program-for-tower-of-hanoi/)'''


def hanoi(n, source, target, spare):
    global count
    if n > 0:
        # move n-1 disks from source to spare, so they are out of the way
        hanoi(n-1, source, spare, target)
        # move the nth disk from source to target
        target.append(source.pop())
        count += 1
        # move the n-1 disks from spare to target
        hanoi(n-1, spare, target, source)


# Initiate call from source A to target C with auxiliary
num_moves = []
for x in range(1, 5):
    # A = [5, 4, 3, 2, 1]
    A = list(range(x, 0, -1))
    B = []
    C = []
    count = 0
    hanoi(x, A, B, C)
    num_moves.append(count)
print(num_moves)
