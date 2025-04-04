from flask import Flask, request, jsonify

app = Flask(__name__)

employees = []

@app.route('/employee', methods=['GET', 'POST'])
def employee_list():
    if request.method == 'GET':
        return jsonify(employees)
    
    if request.method == 'POST':
        data = request.json
        employee = {
            "id": len(employees) + 1,
            "name": data.get("name"),
            "age": data.get("age"),
            "department": data.get("department")
        }
        employees.append(employee)
        return jsonify(employee), 201

@app.route('/employee/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def employee(id):
    employee = next((e for e in employees if e["id"] == id), None)

    if request.method == 'GET':
        return jsonify(employee) if employee else jsonify({"message": "Employee not found"}), 404

    if request.method == 'PUT':
        if employee:
            data = request.json
            employee.update({
                "name": data.get("name", employee["name"]),
                "age": data.get("age", employee["age"]),
                "department": data.get("department", employee["department"])
            })
            return jsonify(employee)
        return jsonify({"message": "Employee not found"}), 404

    if request.method == 'DELETE':
        global employees
        employees = [e for e in employees if e["id"] != id]
        return jsonify({"message": "Employee deleted"})

if __name__ == '__main__':
    app.run(debug=True)
