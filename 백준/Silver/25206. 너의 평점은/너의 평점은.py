grade_list = {
    'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0,
    'F': 0.0, 'P':0.0
}

total_grade = 0
total_credit = 0
for i in range(20):
  subject, credit, grade = input().split()
  credit = float(credit)
  
  if grade == "P":
    continue
  total_credit += credit 
  total_grade += (credit * grade_list[grade])
if total_credit == 0 :
  result = 0.0
else:
  result = total_grade / total_credit
print(f"{result:.6f}")