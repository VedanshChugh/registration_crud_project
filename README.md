# registration_crud_project
This project implements basic CRUD (Create, Read, Update, Delete) operations for a Registration system using MySQL as the database and Python for backend logic.
# Prerequisites
- Python 3.x installed
- MySQL installed and running
- MySQL Connector for Python (`mysql-connector-python`)
# Running the Project
- Ensure MySQL is running.
make sure you created a database and using the database after that use this code to create a table in your database( i create database as: "my_data" and table as:"Registration"
CREATE TABLE Registration (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    DateOfBirth DATE,
    PhoneNumber VARCHAR(15),
    Address TEXT
);

- Run the backend script (`mysql_crud.py`) to interact with the database.
for running the python script without any error replace **user** with **your actual username** , **password** with **your actual password** and **database** with **your database**.
