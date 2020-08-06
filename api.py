from models import app
from flask import jsonify
from crud.teacher_crud import get_all_teachers, get_teacher, create_teacher, update_teacher, destroy_teacher

@app.errorHandler(Exception)
def unhandled_exception(e):
  app.logger.error('Unhandled Exception: %s', (e))
  message_str = e.__str__()
  return jsonify(message=message_str.split(':')[0])

@app.route('/')
def home():
  return jsonify(message="Welcome to Your Teacher Portal")

@app.route('/teachers', methods=['GET', 'POST'])
  def teacher_index_create():
    if request.method == 'GET':
      return get_all_teachers
    if requst.method == 'POST':
      return create_teacher(name=request.form['name'], email=request.form['email'], grade=request.form['grade'])

@app.route('/teachers/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def teacher_show_put_delete(id):
  if request.method == 'GET':
    return get_teacher(id)
  if request.method == 'PUT':
    return update_teacher(id, name=request.form[name], email=request.form[email], grade=reqeust.form[grade])
  if request.method == 'DELETE':
    return destroy_teacher(id)


