student_score ={
'Harry': 88,
'Hermoine': 95,
'Draco' : 45,
'Jinny':85,
'Neville':35

}
# Empty dictionary that will store final grade results
studentGrades = {}
# here we will Loop through each key (student name) in the student_score dictionary
for students in student_score:
 # Retrieving the numeric score for the current student here
  score =student_score[students]
  if score > 90:
    studentGrades[students]= "You Got A"
  elif score > 80:
    studentGrades[students] = "You Got B"
  elif score > 70:
    studentGrades[students] = "You Got C"
  elif score > 60:
    studentGrades[students] = "You Got D"
  else:
    studentGrades[students] = "You Failed"

print(studentGrades)
