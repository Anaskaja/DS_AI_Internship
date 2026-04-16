import json
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# This list of dictionaries is our temporary "database"
employees = [
    { 'id': 1, 'name': 'Ashley' },
    { 'id': 2, 'name': 'Kate' },
    { 'id': 3, 'name': 'Joe' }
]

# A counter to keep track of the next available ID when we add new employees
nextEmployeeId = 4
def get_employee(id):
    # Searches the list and returns the employee if the ID matches
    return next((e for e in employees if e['id'] == id), None)

def employee_is_valid(employee):
    # Checks if the provided data only contains a 'name' key (no extra garbage data)
    for key in employee.keys():
        if key != 'name':
            return False
    return True
# GET ALL EMPLOYEES
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

# GET A SINGLE EMPLOYEE BY ID
@app.route('/employees/<int:id>', methods=['GET'])
def get_employee_by_id(id: int):
    employee = get_employee(id)
    if employee is None:
        return jsonify({ 'error': 'Employee does not exist'}), 404
    return jsonify(employee)
# CREATE A NEW EMPLOYEE
@app.route('/employees', methods=['POST'])
def create_employee():
    global nextEmployeeId
    
    # Read the incoming JSON data
    employee = json.loads(request.data)
    
    # Validate it using our helper function
    if not employee_is_valid(employee):
        return jsonify({ 'error': 'Invalid employee properties.' }), 400

    # Assign an ID and add to our list
    employee['id'] = nextEmployeeId
    nextEmployeeId += 1
    employees.append(employee)

    # Return success (201 Created) and the location of the new record
    return '', 201, { 'location': f'/employees/{employee["id"]}' }
# UPDATE AN EXISTING EMPLOYEE
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id: int):
    employee = get_employee(id)
    if employee is None:
        return jsonify({ 'error': 'Employee does not exist.' }), 404

    updated_employee = json.loads(request.data)
    if not employee_is_valid(updated_employee):
        return jsonify({ 'error': 'Invalid employee properties.' }), 400

    # Update the dictionary with the new data
    employee.update(updated_employee)
    return jsonify(employee)

# DELETE AN EMPLOYEE
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id: int):
    global employees
    employee = get_employee(id)
    if employee is None:
        return jsonify({ 'error': 'Employee does not exist.' }), 404

    # Rebuild the list without the deleted employee
    employees = [e for e in employees if e['id'] != id]
    return jsonify(employee), 200
if __name__ == '__main__':
    # Starts the server on port 5000
    app.run(port=5000)