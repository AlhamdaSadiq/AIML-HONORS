import pandas as pd
import os

class Employee:
    def __init__(self):
        if os.path.exists("employee.csv"):
            self.df = pd.read_csv("employee.csv")
        else:
            self.df = pd.DataFrame(columns=["id", "name", "salary"])

    def add(self):
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        salary = int(input("Enter Salary: "))

        new_record = pd.DataFrame({
            "id": [id],
            "name": [name],
            "salary": [salary]
        })

        self.df = pd.concat([self.df, new_record], ignore_index=True)
        self.df.to_csv("employee.csv", index=False)

        print("Record added")

    def display(self):
        print(self.df)

    def update(self):
        id = int(input("Enter ID: "))
        salary = int(input("Enter new salary: "))

        if id in self.df["id"].values:
            self.df.loc[self.df["id"] == id, "salary"] = salary
            self.df.to_csv("employee.csv", index=False)
            print("Record updated")
        else:
            print("Employee not found")

    def delete(self):
        id = int(input("Enter ID: "))

        if id in self.df["id"].values:
            self.df = self.df[self.df["id"] != id]
            self.df.to_csv("employee.csv", index=False)
            print("Record deleted")
        else:
            print("Employee not found")


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
