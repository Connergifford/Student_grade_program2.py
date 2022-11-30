student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

scores = student_scores.copy()
for key, value in scores.items():
    if value >= 91:
        scores[key] = 'Outstanding'
    if value <= 90 and value >= 81:
        scores[key] = 'Exceeds Expectations'
    if value <= 80 and value >= 71:
        scores[key] = 'Acceptable'
    elif value <= 70:
        scores[key] = 'Fail'
print(scores)    
#Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}



#TODO-2: Write your code below to covert scores into grades.👇
#Hint: Use a for loop here.
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = 'Outstanding'
    elif score > 80:
        student_grades[student] = 'Exceeds Expectations'
    elif score > 70:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"
   

#Don't change the code below 👇
print(student_grades)
