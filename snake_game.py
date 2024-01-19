score = 90
grade = ''

if score >= 93:
    grade = 'A'
if (score >= 84 or score <= 92):
	grade = 'B'
if (score >= 75 or score <= 83):
	grade = 'C'
if (score < 75):
	grade = 'F'
	
print(grade)

if (score >= 93):
	grade = 'A'
if (84 <= score <= 92):
	grade = 'B'
if (75 <= score <= 83):
	grade = 'C'
if (score < 75):
	grade = 'F'
	
print(grade)

if (score > 92):
	grade = 'A'
elif (score > 83):
	grade = 'B'
elif (score > 74):
	grade = 'C'
else:
	grade = 'F'

print(grade)