def gradingStudents(grades):
    for grade in grades:
        if grade > 38 and grade % 5 > 2: grade = ((grade//5) * 5) + 5
        print(grade)

if __name__ == '__main__':
    grades = []
    for _ in range(int(input())):
        grades.append(int(input()))
    gradingStudents(grades)