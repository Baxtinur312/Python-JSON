import json

with open('students.json', 'r') as file:
 students = json.loads(file.read())
# Sort students by rating in descending order
students.sort(key=lambda x: x['score'], reverse=True)
with open('rating.json', 'w') as file:
    file.write(json.dumps(students, indent=4))
