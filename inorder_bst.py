def average_marks(student_marks, query_name):
    marks = student_marks[query_name]
    average = sum(marks) / len(marks)
    return "{:.2f}".format(average)

if __name__ == '_main_':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print(average_marks(student_marks, query_name))