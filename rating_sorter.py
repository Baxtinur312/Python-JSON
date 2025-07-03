import json

with open('students.json', 'r') as file:
    students = json.load(file)

# Sort students by score in descending order
sorted_students = sorted(students, key=lambda x: x['score'], reverse=True)
ranked_students = [f"{i+1},{student['name']},{student['score']}\n" for i, student in enumerate(sorted_students)]

with open('rating.csv', 'w') as f:
    f.write('Rank,Name,Rating\n')
    f.writelines(ranked_students)
