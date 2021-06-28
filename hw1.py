import score

ban = []
count = 5

for i in range(0, count, 1):
    student = []
    student.append(input('성명: '))
    student.append(int(input('국어점수: ')))
    student.append(int(input('영어점수: ')))
    student.append(int(input('수학점수: ')))

    ban.append(student)

print()
for i in range(0, count, 1):
    ban[i].append(score.total(ban[i]))
    ban[i].append(score.ave(ban[i]))
    ban[i].append(score.grade(ban[i]))

    score.output(ban[i])

print()
print('2명 성적 비교하여 더 좋은 점수의 학생 찾기')
score.output(ban[2])
score.output(ban[4])
print('성적이 더 좋은 학생')
score.output( score.max_student(ban[2], ban[4]) )

print()
print('3명 성적 비교하여 가장 좋은 점수의 학생 찾기')
score.output(ban[1])
score.output(ban[2])
score.output(ban[3])
print('성적이 가장 좋은 학생')
score.output( score.max_student(ban[1], ban[2], ban[3]) )
