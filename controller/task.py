from controller import app
from flask import render_template, jsonify, request, Response
import json
from model.task import Task

task = Task()

@app.route('/')
def load_app():
  return render_template('index.html')

@app.route('/api/task/', methods=['GET', 'POST'])
def show_task():
  response = []

  if request.method == 'POST':
    response = task.create(request.form)
    code = 201
  else:
    response = task.list()
    code = 200

  return jsonify(response), code, {'Content-Type': 'application/json'}

@app.route('/api/task/done/<int:task_id>')
def task_done(task_id):
  response = task.done(task_id)

  return jsonify(response), 200, {'Content-Type': 'application/json'}