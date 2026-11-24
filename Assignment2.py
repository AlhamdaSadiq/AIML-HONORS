import csv
import os

class Employee:

    def __init__(self):
        self.file = "employee.csv"

    def create(self):
        with open(self.file, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["ID", "Name", "Salary"])
            print("Employee file created.")

    def add(self):
        if not os.path.exists(self.file):
            print("Create file first!")
            return

        with open(self.file, "a", newline="") as f:
            w = csv.writer(f)
            id = input("Enter ID: ")
            name = input("Enter Name: ")
            salary = input("Enter Salary: ")
            w.writerow([id, name, salary])
            print("Employee added.")

    def display(self):
        if not os.path.exists(self.file):
            print("File does not exist!")
            return

        with open(self.file, "r") as f:
            for row in csv.reader(f):
                print(row)

    def update(self):
        if not os.path.exists(self.file):
            print("File does not exist!")
            return

        with open(self.file, "r") as f:
            rows = list(csv.reader(f))

        id = input("Enter ID to update: ")
        found = False

        for row in rows[1:]:
            if row[0] == id:
                row[1] = input("Enter new name: ")
                row[2] = input("Enter new salary: ")
                found = True
                break

        if found:
            with open(self.file, "w", newline="") as f:
                csv.writer(f).writerows(rows)
            print("Employee updated.")
        else:
            print("Employee ID not found.")

    def delete(self):
        if not os.path.exists(self.file):
            print("File does not exist!")
            return

        with open(self.file, "r") as f:
            rows = list(csv.reader(f))

        id = input("Enter ID to delete: ")
        new_rows = [rows[0]]

        for row in rows[1:]:
            if row[0] != id:
                new_rows.append(row)

        if len(new_rows) == len(rows):
            print("Employee ID not found.")
        else:
            with open(self.file, "w", newline="") as f:
                csv.writer(f).writerows(new_rows)
            print("Employee deleted.")

e = Employee()

while True:
    print("\n1. Create  2. Add  3. Display  4. Update  5. Delete  6. Exit")

    try:
        ch = int(input("Enter choice: "))

        if ch == 1:
            e.create()
        elif ch == 2:
            e.add()
        elif ch == 3:
            e.display()
        elif ch == 4:
            e.update()
        elif ch == 5:
            e.delete()
        elif ch == 6:
            break
        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter a valid number.")
