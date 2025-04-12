#元组排序练习

#复杂的排序 列表里面每个元素都是一个元组 tuple 

students = [
    ("张坤", 180, 'A'),
    ("李华", 175, 'B'),
    ("李时珍", 183, 'A'),
    ("康思远", 190, 'D'),
    ("鑫佳佳", 160, 'E')
]

sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)

sorted_students = sorted(students, key=lambda student: student[2])
print(sorted_students)

sorted_students = sorted(students, key=lambda student: student[0])
print(sorted_students)