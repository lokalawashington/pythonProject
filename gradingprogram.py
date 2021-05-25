student_score = {
    "harry":81,
    "ron": 78,
    "washington": 99,
    "draco": 74,
    "neville": 62
}

student_grade = {}
for student in student_score:
    score = student_score[student]
    if score > 90:
        student_grade[student] = "outstanding"
    if score > 80:
        student_grade[student] = "exceeds expectations"
    if score > 80:
        student_grade[student] = "acceptable"
    else:
        student_grade[student] = "fail"

print(student_grade)