import csv

class Employee:
    def __init__(self):
        self.file = "employee.csv"

    def create(self):
        with open(self.file, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["ID", "Name", "Salary"])
            print("Employee file created.")

    def add(self):
        with open(self.file, "a", newline="") as f:
            w = csv.writer(f)
            id = input("Enter ID: ")
            name = input("Enter Name: ")
            salary = input("Enter Salary: ")
            w.writerow([id, name, salary])

    def display(self):
        with open(self.file, "r") as f:
            for row in csv.reader(f):
                print(row)

    def update(self):
        rows = list(csv.reader(open(self.file)))
        id = input("Enter ID to update: ")

        for row in rows:
            if row[0] == id:
                row[1] = input("Enter new name: ")
                row[2] = input("Enter new salary: ")

        with open(self.file, "w", newline="") as f:
            csv.writer(f).writerows(rows)

    def delete(self):
        rows = list(csv.reader(open(self.file)))
        id = input("Enter ID to delete: ")
        rows = [row for row in rows if row[0] != id]

        with open(self.file, "w", newline="") as f:
            csv.writer(f).writerows(rows)


e = Employee()

while True:
    print("\n1. Create  2. Add  3. Display  4. Update  5. Delete  6. Exit")
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
