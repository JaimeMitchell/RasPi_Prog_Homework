grade_list = []
grade_sum = 0
stu_num = int(input('Enter amount of students: '))
for i in range(stu_num):
    stu_name = input("Enter student's name: ")
    stu_grade = int(input("Enter student's grade: "))
    grade_sum += stu_grade
    stu_dict = {'name': stu_name, 'grade': stu_grade}
    grade_list.append(stu_dict)



for i in grade_list:
    print(f'{i["name"]} = {i["grade"]}')
#print precision to 2 decimal places
print(f"average grade = {grade_sum/stu_num:.2f}")







