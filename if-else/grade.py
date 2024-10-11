total_marks = int(input('what is your total score out of 100?\n'))
if total_marks>= 95:
    grade = 'O'
elif total_marks>=90 and total_marks<95:
    grade = 'A'
elif total_marks>=80 and total_marks<90:
    grade = 'B'
elif total_marks>=70 and total_marks<80:
    grade = 'C'
elif total_marks>=50 and total_marks<70:
    grade = 'D'
elif total_marks>=40 and total_marks<40:
    grade = 'P'
else:
    grade = 'F'
print(f'after scoring {total_marks} you got {grade} grade')