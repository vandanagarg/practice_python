''' String formatting '''


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        # print(name, scores)
        student_marks[name] = scores
    query_name = input()

    # print(student_marks[query_name])
    print("%.2f" % ((sum(student_marks[query_name]) / len(
        student_marks[query_name]))))
    print("{:.2f}".format((sum(student_marks[query_name]) / len(
        student_marks[query_name]))))
    # print("%.2f"%(average_marks))

# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
