# Brandon Ching
# CSCI102 - Section C
# Python-GradeCalculation00

maxGrade = [float(input()),float(input()),float(input()),float(input())]
studentScores = [int(input()),int(input()),int(input()),int(input())]
eachScore = []
i = 0

while i <= 3:
    eachScore.append((studentScores[i]/maxGrade[i])*100)
    i = i + 1

avgScore = sum(eachScore)/len(eachScore)
maxScore = max(eachScore)
minScore = min(eachScore)

print(
    f"Average score: {avgScore:.2f}% "
    f"| Max: {maxScore:.2f}% "
    f"| Min: {minScore:.2f}%"
    )
