from mymodules.models import Student
from mymodules.math_utils import average_grade

def main(self):
    yohannes = Student('Yohannes Berhane', 96)
    henok = Student("Henok Asfaw", 90)
    garrison = Student('Garrison Harte', 88)
    zach = Student('Zach Heberer', 85)
    brandon = Student("Brandon Dow", 82)
    xavier = Student('Xavier Celestino', 94)
    anthony = Student("Anthony Pavone", 91)
    aidan = Student('Aidan Stahly', 84)
    joshua = Student('Joshua Meka', 83)
    joe = Student('Joe Loch', 78)

    studentsList = []
    studentsList.append(yohannes)
    studentsList.append(henok)
    studentsList.append(garrison)
    studentsList.append(zach)
    studentsList.append(brandon)
    studentsList.append(xavier)
    studentsList.append(anthony)
    studentsList.append(aidan)
    studentsList.append(joshua)
    studentsList.append(joe)

    for stu in studentsList:
        print("- " + stu.student_name + stu.student_grade)

    average_grade(students)
