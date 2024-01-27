from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, Session

engine = create_engine('sqlite:///example.db', echo=True)

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship('Student', back_populates='course')

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    course_id = Column(Integer, ForeignKey('courses.id'))
    course = relationship('Course', back_populates='students')

Base.metadata.create_all(engine)

session = Session(engine)

course1 = Course(name='Math')
course2 = Course(name='Physics')

student1 = Student(name='Alice', course=course1)
student2 = Student(name='Bob', course=course1)
student3 = Student(name='Charlie', course=course2)

session.add_all([course1, course2, student1, student2, student3])
session.commit()

math_students = session.query(Student).join(Course).filter(Course.name == 'Math').all()

for student in math_students:
    print(f"Student {student.name} is enrolled in the {student.course.name} course")

session.close()
