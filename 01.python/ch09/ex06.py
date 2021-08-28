score = [
    [88, 76, 92, 98],
    [65, 70, 58, 82],
    [82, 80, 78, 88]
]

total = 0
totalsub = 0
for student in score:
    subject_total = 0
    for subject in student:
        subject_total += subject
    subjects = len(student)
    average = subject_total / subjects
    print(f"총점 {subject_total}, 평균 {average:.2f}")
    total += subject_total
    totalsub += subjects
total_average = total / totalsub
print(f"전체평균 {total_average:.2f}")
