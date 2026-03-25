from flask import Blueprint, request, jsonify
from app.database import get_db_connection

emp_bp = Blueprint("employees", __name__)




@emp_bp.route("/employees", methods=["POST"])
def create_employee():
    data = request.get_json()

    name = data.get("name")
    role = data.get("role")
    salary = data.get("salary", 0)
    bonus = data.get("bonus", 0)

    if role not in ["manager", "staff"]:
        return jsonify({"error": "Invalid role"}), 400
    
    if role == "staff":
        bonus = 0
    
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO employees (name, role, salary, bonus) VALUES (?, ?, ?, ?)", (name, role, salary, bonus))
    conn.commit()
    emp__id = cursor.lastrowid
    conn.close()

    return jsonify({"message": "Employee created successfully", "id": emp__id}), 201


@emp_bp.route("/employees", methods=["GET"])
def get_employees():
    conn = get_db_connection()
    cursor = conn.cursor()

    employees = cursor.execute("SELECT * FROM employees").fetchall()
    conn.close()

    return jsonify([dict(e) for e in employees]), 200



@emp_bp.route("/employees/<int:emp_id>", methods=["PUT"])
def update_employee(emp_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    employee = cursor.execute("SELECT * FROM employees WHERE id = ?", (emp_id,)).fetchone()
    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    data = request.get_json()

    name = data.get("name")
    role = data.get("role")
    salary = data.get("salary")
    bonus = data.get("bonus", 0)

    if role not in ["manager", "staff"]:
        return jsonify({"error": "Invalid role"}), 400
    
    if role == "staff":
        bonus = 0

   

    cursor.execute("UPDATE employees SET name = ?, role = ?, salary = ?, bonus = ? WHERE id = ?", (name, role, salary, bonus, emp_id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Employee updated successfully"}), 200


@emp_bp.route("/employees/<int:emp_id>", methods=["DELETE"])
def delete_employee(emp_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    employee = cursor.execute("SELECT * FROM employees WHERE id = ?", (emp_id,)).fetchone()
    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    cursor.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Employee deleted successfully"}), 200

    
