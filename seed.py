from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from faker import Faker
import random
from datetime import date, timedelta
from models import Base, Group, Teacher, Subject, Student, Grade

# Налаштування бази даних
engine = create_engine('sqlite:///university.db')
Session = sessionmaker(bind=engine)
session = Session()

# Ініціалізація Faker
faker = Faker()

# Заповнення груп
groups = [Group(name=f"Group {chr(65 + i)}") for i in range(3)]
session.add_all(groups)
session.commit()

# Заповнення викладачів
teachers = [Teacher(name=faker.name()) for _ in range(5)]
session.add_all(teachers)
session.commit()

# Заповнення предметів
subjects = [Subject(name=sub, teacher=random.choice(teachers)) for sub in ["Math", "Physics", "Chemistry", "Biology", "History", "Literature", "Programming", "Philosophy"]]
session.add_all(subjects)
session.commit()

# Заповнення студентів
students = [Student(name=faker.name(), group=random.choice(groups)) for _ in range(50)]
session.add_all(students)
session.commit()

# Заповнення оцінок
for student in students:
    for _ in range(random.randint(15, 20)):
        grade = Grade(
            student=student,
            subject=random.choice(subjects),
            grade=random.uniform(60, 100),
            date_received=date.today() - timedelta(days=random.randint(0, 365))
        )
        session.add(grade)

session.commit()
print("Database seeded successfully!")
