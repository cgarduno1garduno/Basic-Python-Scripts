################################################################################
## Cristopher Garduno Luna
##
## Introductory python scripts for Codecademy 
##   These functions calculate student's average scores and return 
##   final scores + final letter grade
##     homework: 10% of final grade
##     quizzes : 30% of final grade
##     exams   : 60% of final grade
################################################################################

# student data
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# input list of numbers and compute average
def average(x):
    total = float(sum(x))
    return total/len(x)
   
# get student's weighted average score
def get_average(student):
    homework = .1*average(student["homework"])
    quizzes  = .3*average(student["quizzes"])
    tests    = .6*average(student["tests"])
    return homework+quizzes+tests

# return letter grade based on weighted average score
def get_letter_grade(score):
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    return "F"

# get class average
def get_class_average(students):
    results = []
    for s in students:
        results.append(get_average(s))
    return average(results)
    
# show class average score and letter grade
print get_class_average(students), get_letter_grade(get_class_average(students))
