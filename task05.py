import random as rnd
from collections import namedtuple

Student = namedtuple('Student', 'name, age, grade, country')

students = (
    Student("Алексей", rnd.randint(18, 25), round(rnd.random() * 7 + 3, 2), "Минск"),
    Student("Мария", rnd.randint(18, 25), round(rnd.random() * 7 + 3, 2), "Гродно"),
    Student("Иван", rnd.randint(18, 25), round(rnd.random() * 7 + 3, 2), "Брест"),
    Student("Ольга", rnd.randint(18, 25), round(rnd.random() * 7 + 3, 2), "Витебск"),
    Student("Дмитрий", rnd.randint(18, 25), round(rnd.random() * 7 + 3, 2), "Гомель"),
    Student("Светлана", rnd.randint(18, 25), round(rnd.random() * 7 + 3, 2), "Минск"),
    Student("Павел", rnd.randint(18, 25), round(rnd.random() * 7 + 3, 2), "Могилёв"),
)

print("Студенты: ")
for student in students:
    print(f"Имя: {student.name}, возраст: {student.age}, оценка: {student.grade}, страна: {student.country}")

avg = sum(student.grade for student in students) / len(students)
goodStudents = filter(lambda s: s.grade >= avg, students)

print(f"\nУченики {", ".join(map(lambda s: s.name, goodStudents))} в этом семестре хорошо учатся!")