from openpyxl.workbook import Workbook
# ==============================
# Part 1: Employee & Professor
# ==============================
class Employee:
    def __init__(self, emp_id, name, salary):
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = salary

    # Getters
    def get_emp_id(self):
        return self.__emp_id

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    # Setter
    def set_salary(self, salary):
        self.__salary = salary


class Professor(Employee):
    def __init__(self, emp_id, name, salary, subject):
        super().__init__(emp_id, name, salary)
        self.subject = subject

    def display_details(self):
        print("Professor Details")
        print("------------------")
        print("ID:", self.get_emp_id())
        print("Name:", self.get_name())
        print("Salary:", self.get_salary())
        print("Subject:", self.subject)


# Create object and display
prof = Professor(11, "Harry", 90000, "Engineering Physics")
prof.display_details()


# ==============================
# Part 2: CSV File Handling
# ==============================
import csv
import pandas as pd

# Write CSV using csv module
data_csv = [
    ['Name', 'Age', 'City'],
    ['Asha', 22, 'Kathmandu'],
    ['Ramesh', 25, 'Pokhara']
]

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_csv)

# Write CSV using pandas
data_pd = {
    'Name': ['Asha', 'Ramesh'],
    'Age': [22, 25],
    'City': ['Kathmandu', 'Pokhara']
}
df = pd.DataFrame(data_pd)
df.to_csv('output1.csv', index=False)

# Read CSV using csv module
with open('output.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Read CSV using pandas
output = pd.read_csv('output.csv')
print(output)


# ==============================
# Part 3: JSON File Handling
# ==============================
import json

data_json = [
    {"Name": "Asha", "Age": 22},
    {"Name": "Ramesh", "Age": 25}
]

with open('output.json', 'w') as file:
    json.dump(data_json, file, indent=4)


# ==============================
# Part 4: TXT File Handling
# ==============================
students = [
    "1, Ram, 85\n",
    "2, Sita, 90\n",
    "3, Hari, 78\n"
]

with open("students.txt", 'w') as file:
    file.writelines(students)

# Read TXT file
with open("students.txt", "r") as file:
    content = file.read()

print("\nReading data from file:")
print(content)


# ==============================
# Part 5: Excel File Handling
# ==============================
data_excel = {
    "ID": [1, 2, 3],
    "Name": ["Ram", "Sita", "Hari"],
    "Marks": [85, 90, 78]
}

df_excel = pd.DataFrame(data_excel)
df_excel.to_excel("students.xlsx", index=False)

# Read Excel
df_read = pd.read_excel("students.xlsx")
print(df_read)
