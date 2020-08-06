from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/flasql'
app.config['FLASK_ENV'] = 'development'
app.config['FLASK_APP'] = 'api.py'

db = SQLAlchemy(app)

class Teacher(db.Model):
  __tablename__ = 'teachers'

  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String, unique=True, nullable=False)
  name = db.Column(db.String, nullable=False)
  grade = db.Column(db.String)

  students = db.relationship('Student', backref='teacher', lazy=True)

  def as_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "email": self.email,
      "bio": self.bio
    }
    
  def __repr__(self):
    return f'Teacher(id={self.id}, email="{self.email}", name="{self.name}", grade="{self.grade}")'

student_assignments = db.Table('student_assignments'
  db.Column('student_id', db.Integer, db.ForeignKey('students.id'), primary_key=True),
  db.Column('assignment_id', db.Integer, db.ForeignKey('assigments.id'), primary_key=True)
)

class Student(db.Model):
  __tablename__ = 'students'

  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String, unique=True, nullable=False)
  name = db.Column(db.String, nullable=False)
  teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))

  assignments = db.relationship('Assignment', secondary=student_assignments, lazy='subquery', back_populates='students')

  def __repr__(self):
    return f'Student(id={self.id}, email="{self.email}" name="{self.name}")'

class Assignment(db.Model):
  __tablename__ = 'assignments'

  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String)
  grade = db.Column(db.String)

  students = db.relationship('Student', secondary=student_assignments, lazy=True, back_populates="assignments")

  def __repr__(self):
    return f'Assignment(id={self.id}, description="{self.description}", grade="{self.grade}")'