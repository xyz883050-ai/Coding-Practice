# ETL Code
import mysql.connector

# Connect MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

print("Connected Successfully")

cursor = conn.cursor(dictionary=True)

# Extract Data
cursor.execute("SELECT * FROM students_info")
students = cursor.fetchall()

cursor.execute("SELECT * FROM roll_numbers")
rolls = cursor.fetchall()

# Create New Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS merged_data(
    name VARCHAR(100),
    roll_id INT,
    marks INT,
    roll_no INT,
    class VARCHAR(20)
)
""")

# Transform + Load
for s in students:
    for r in rolls:

        if s['name'] == r['student_name']:

            cursor.execute("""
            INSERT INTO merged_data
            VALUES(%s,%s,%s,%s,%s)
            """, (
                s['name'],
                s['roll_id'],
                s['marks'],
                r['roll_no'],
                r['class']
            ))

# Save Changes
conn.commit()

# Display Output
cursor.execute("SELECT * FROM merged_data")

result = cursor.fetchall()

print("\nMerged Data:\n")

for row in result:
    print(row)

# Close Connection
conn.close()