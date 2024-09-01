student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

student_grades = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

for i in student_scores:
    if student_scores[i] <= 70:
        student_grades[i] = "Fail"
    elif student_scores[i] >= 71 and student_scores[i] <= 80:
        student_grades[i] = "Acceptable"
    elif student_scores[i] >= 81 and student_scores[i] <= 90:
        student_grades[i] = "Exceeds Expectations"
    else:
        student_grades[i] = "Outstanding"

print(student_grades)
