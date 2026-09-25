import sqlite3
import pandas as pd

class Employee:
    def __init__(self):
        self.con = sqlite3.connect("employee.db")
        self.cur = self.con.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS employee "
            "(ID INTEGER PRIMARY KEY, Name TEXT, Salary INTEGER)"
        )

    def add(self):
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        salary = int(input("Enter Salary: "))

        self.cur.execute(
            "INSERT INTO employee VALUES(?,?,?)",
            (id, name, salary)
        )
        self.con.commit()

    def display(self):
        df = pd.read_sql("SELECT * FROM employee", self.con)
        print(df)

    def update(self):
        id = int(input("Enter ID: "))
        salary = int(input("Enter new salary: "))

        self.cur.execute(
            "UPDATE employee SET Salary=? WHERE ID=?",
            (salary, id)
        )
        self.con.commit()

    def delete(self):
        id = int(input("Enter ID: "))
        self.cur.execute(
            "DELETE FROM employee WHERE ID=?", (id,)
        )
        self.con.commit()


e = Employee()

while True:
    print("\n1.Add  2.Display  3.Update  4.Delete  5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        e.add()
    elif ch == 2:
        e.display()
    elif ch == 3:
        e.update()
    elif ch == 4:
        e.delete()
    elif ch == 5:
        break
