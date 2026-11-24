import sqlite3

class Employee:
    def __init__(self):
        self.con = sqlite3.connect("employee.db")
        self.cur = self.con.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY, name TEXT, salary INTEGER)"
        )

    def add(self):
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        salary = int(input("Enter Salary: "))
        self.cur.execute("INSERT INTO employee VALUES(?,?,?)",
                         (id, name, salary))
        self.con.commit()
        print("Record added")

    def display(self):
        self.cur.execute("SELECT * FROM employee")
        for row in self.cur.fetchall():
            print(row)

    def update(self):
        id = int(input("Enter ID: "))
        salary = int(input("Enter new salary: "))
        self.cur.execute("UPDATE employee SET salary=? WHERE id=?",
                         (salary, id))
        self.con.commit()
        print("Record updated")

    def delete(self):
        id = int(input("Enter ID: "))
        self.cur.execute("DELETE FROM employee WHERE id=?", (id,))
        self.con.commit()
        print("Record deleted")


e = Employee()

while True:
    print("\n1. Add")
    print("2. Display")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

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
    else:
        print("Invalid choice")
