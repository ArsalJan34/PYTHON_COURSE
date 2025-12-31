Student_scores = [ 150,142,185,120,199,200,45,9,104,54,89,69,134,99,146]
total_exam_score = sum(Student_scores)
sum = 0
for score in Student_scores:
  sum += score
print(sum)
print(max(Student_scores))
max_score = 0
for score in Student_scores:
  if score > max_score:
    max_score =score
    print(max_score)

