import mysql.connector

db = mysql.connector.connect(
    host="localhost",       
    user="root",     
    password="", # Replace with your MySQL password
    database="my_data"     
)
cursor = db.cursor()
def create_user(name, email, dob, phone, address):
    sql = "INSERT INTO Registration (Name, Email, DateOfBirth, PhoneNumber, Address) VALUES (%s, %s, %s, %s, %s)"
    values = (name, email, dob, phone, address)
    cursor.execute(sql, values)
    db.commit()
    print(f"User {name} added successfully!")
def read_users():
    cursor.execute("SELECT * FROM Registration")
    for user in cursor.fetchall():
        print(user)
def update_user(user_id, new_name):
    sql = "UPDATE Registration SET Name = %s WHERE ID = %s"
    values = (new_name, user_id)
    cursor.execute(sql, values)
    db.commit()
    print(f"User ID {user_id} updated to {new_name}!")
def delete_user(user_id):
    sql = "DELETE FROM Registration WHERE ID = %s"
    cursor.execute(sql, (user_id,))
    db.commit()
    print(f"User ID {user_id} deleted!")
create_user("John Doe", "john@example.com", "1990-01-01", "1234567890", "123 Main St")
read_users()
update_user(1, "John Smith")
delete_user(1)
