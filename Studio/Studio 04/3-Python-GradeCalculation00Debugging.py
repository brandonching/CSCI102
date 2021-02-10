# Brandon Ching
# CSCI102 - Section C
# Python-GradeCalculation00

#enter max grades for each assignment
Max_grade = [float(input()),float(input()),float(input()),float(input())]

#enter student's scores for each assignment
grade = [int(input()),int(input()),int(input()),int(input())]

#calculate student's grades in percentage form for each assignment
Pgrade = [grade[0]/Max_grade[0],grade[1]/Max_grade[1],grade[2]/Max_grade[2],grade[3]/Max_grade[3]]

#calculate average, and min grades
average_grade = sum(Pgrade)/len(Pgrade)*100
max_grade = max(Pgrade)*100
min_grade = min(Pgrade)*100

#format print statement
print(f"Average score: {average_grade:.2f}% | Max: {max_grade:.2f}% | Min: {min_grade:.2f}%")
