def total(student):
    if student is None:
        return 0
    elif len(student) < 4:
        return 0
    
    return student[1]+student[2]+student[3]

def ave(student):
    if student is None:
        return 0
    elif len(student) < 5:
        return 0
    
    return student[4]/3

def grade(student):
    if student is None:
        return ''
    elif len(student) < 6:
        return ''
    
    if student[5] >= 90:
        return 'A'
    elif student[5] >= 80:
        return 'B'
    elif student[5] >= 70:
        return 'C'
    elif student[5] >= 60:
        return 'D'
    else:
        return 'F'

def output(student):
    if student is not None:
        if len(student) >= 7:
            print('%s : 국어 :%d  영어:%d  수학:%d  총점:%d  평균:%.2f  학점:%s' %(student[0], student[1], student[2], student[3], student[4], student[5], student[6]))

def max_student(*student):
    max1 = -1
    maxStudent = []

    for i in range(0, len(student), 1):
        if student[i] is not None:
            if len(student[i]) >= 7:
                if max1 < student[i][4]:
                    max1 = student[i][4]
                    maxStudent = student[i]

    return maxStudent
