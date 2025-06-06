# This program interactively asks about your exam marks, and reports the
# corresponding grades.
#
# Usage:
#
# $ python exam_results.py
#
# A session with the program might look like the following:
#
# $ python exam_results.py
# What marks did you get in Maths?
# > 63
# What marks did you get in Philosophy?
# > 54
# What marks did you get in Geography?
# > 71
# What marks did you get in Music?
# > 68
#
# Your grades:
#
# Maths: B
# Philosophy: C
# Geography: A
# Music: B

subjects = ['Maths', 'Philosophy', 'Geography', 'Music']

grade_boundaries = {
    'A': [70, 100],
    'B': [60, 69],
    'C': [50, 59],
    'D': [40, 49],
    'E': [30, 39],
    'F': [0, 29],
}

student_marks = {}
student_grades = {}

def main():
    get_marks()
    get_grades()
    print_grades()


def get_marks():
    for subject in subjects:
        mark = input(f"What marks did you get in {subject}? ")
        student_marks[subject] = int(mark)

def get_grades():
    for subject, mark in student_marks.items():
        for grade, boundary in grade_boundaries.items():
            if boundary[0] <= mark <= boundary[1]:
                student_grades[subject] = grade
                break

def print_grades():
    print("\nYour grades:\n\n" + "\n".join(f"{subject}: {grade}" for subject, grade in student_grades.items()))



if __name__ == "__main__":
    main()

# TODO:
# * Implement the program as described in the comments at the top of the file.

# TODO (extra):
# * Modify the program to handle the case where the user enters an invalid mark
#   (such as 150, or -25.5, or "bananas")
# * Modify the program to ask the user for the subjects that they've taken.
