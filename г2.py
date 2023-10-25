students = [
    {'id': 1, 'full_name': 'Алекберов Рамиль Русланович'},
    {'id': 2, 'full_name': 'Бобровская Анастасия Дмитриевна'},
    {'id': 3, 'full_name': 'Винговатов Александр Олегович'}
]

full_names = [student['full_name']
              for student
              in students
              if len(student['full_name'].split()[1]) > 6]
print(full_names)
