
def average_grade(roster):
    total_grade = 0
    for stu in roster:
        total_grade = total_grade + stu.student_grade
    avg_grade = total_grade/10
    print("The Average Grade of Current Student Roster is: " + avg_grade)
