students = {'Андрей', 'Дима', 'Максим', 'Стас', 'Антон'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

students = sorted(students)
avg_list = []

for i in grades:
    avg_ = sum(i) / len(i)
    avg_list. append(avg_)

grade_st = zip(students, avg_list)
print(dict(grade_st))