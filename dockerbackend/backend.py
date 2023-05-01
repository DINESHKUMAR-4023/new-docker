from flask import Flask, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
  host="database",
  user="user",
  password="pass",
  database="mydb"
)


cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS students (reg_no INT, name VARCHAR(255), vaccinated BOOLEAN)")
cursor.execute("INSERT INTO students (reg_no, name, vaccinated) VALUES (123, 'John Doe', True)")

db.commit()

@app.route('/vaccination-status', methods=['POST'])
def vaccination_status():
    reg_no = request.json['reg_no']
    cursor.execute(f"SELECT vaccinated FROM students WHERE reg_no = {reg_no}")
    result = cursor.fetchone()
    if result is None:
        return 'Student not found', 404
    else:
        return 'Vaccinated' if result[0] else 'Not vaccinated', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

