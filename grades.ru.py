grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = (list(students))
students = sorted(students)
print(students)
average_score = []
Aaron = average_score.append(sum(grades[0])/len(grades[0]))
Bilbo = average_score.append(sum(grades[1])/len(grades[1]))
Johnny = average_score.append(sum(grades[2])/len(grades[2]))
Khendrik = average_score.append(sum(grades[3])/len(grades[3]))
Steve = average_score.append(sum(grades[4])/len(grades[4]))
print(dict(zip(students,grades)))
print(dict(zip(students,average_score)))

