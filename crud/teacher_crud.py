from flask import jsonify
from models import app, Teacher
from crud.teacher_crud import get_all_teachers

def get_all_teachers():
  all_teachers = Teacher.query.all()
  results = []
  for teacher in all_teachers:
    results.append(teacher.as_dict())
  return jsonify(results)

def get_teacher(id):
  teacher = Teacher.query.get(id)
  if teacher:
    return jsonify(teacher.as_dict())
  else:
    raise Exception('Error at getting teacher at {}'.format(id))

def create_teacher(name, email, grade):
  new_teacher = Teacher(name=name, email=email, grade=grade or None)
  db.session.add(new_teacher)
  db.session.commit()
  return jsonify(new_user.as_dict())

def update_teacher(id, name, email, grade):
  teacher = Teacher.query.get(id)
  if teacher:
    teacher.name = name or teacher.name
    teacher.email = email or teacher.email
    teacher.grade = grade or teacher.grade
    db.session.commit()
    return jsonify(teacher.as_dict())
  else:
    raise Exception('No teacher at id {}'.format(id))

def destroy_teacher(id):
  teacher = Teacher.query.get(id)
  if teacher:
    db.session.delete(teacher)
    db.session.commit()
    return redirect('/teachers')
  else:
    raise Exception('No teacher at id {}'.format(id))