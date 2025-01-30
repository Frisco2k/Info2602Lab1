
# task 3
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
        data = json.load(f)

@app.route('/')
def hello_world():
    return 'Hello, World!' # return 'Hello World' in response

#task 5
@app.route('/students')
def get_students():
  result = []
  pref = request.args.get('pref') # get the parameter from url
  if pref:
    for student in data: # iterate dataset
      if student['pref'] == pref: # select only the students with a given meal preference
        result.append(student) # add match student to the result
    return jsonify(result) # return filtered set if parameter is supplied
  return jsonify(data) # return entire dataset if no parameter supplied

#task 4
@app.route('/students/<id>')
def get_student(id):
  for student in data: 
    if student['id'] == id: # filter out the students without the specified id
      return jsonify(student)
    
#exercise 1 
@app.route('/stats')
def get_stats():
   stats = {
      "Fish" : 0,
      "Chicken" : 0,
      "Vegetable" : 0,
      "Computer Science (Major)" : 0,
      "Computer Science (Special)" : 0,
      "Information Technology (Major)" : 0,
      "Information Technology (Special)" : 0,
   }

   for student in data:
      if student['programme'] in stats:
         stats[student['programme']] += 1 

      if student['pref'] in stats:
         stats[student['pref']] += 1
    
   return jsonify(stats)     

#exercise 2
@app.route('/add/<int:x>/<int:y>')
def addition(x, y):
   return jsonify (x + y)

@app.route('/subtract/<int:x>/<int:y>')
def subtraction(x, y):
   return jsonify (x - y)

@app.route('/multiply/<int:x>/<int:y>')
def multiplication(x, y):
   return jsonify (x * y)


@app.route('/divide/<int:x>/<int:y>')
def division(x, y):
   return jsonify (x / y)


app.run(host='0.0.0.0', port=8080)

