from dbconnect import connect
import sys
sys.path.insert(0, "C:/Users/disga/Desktop/Studium SWB/SWB 3/Softwaretechnik/Labor/Waterfall STC/Softwaretechnik_2022/src/")
from components.stakeholder.Employee import Employee


class sqlfunctions(Employee):

    def insert_new_employee(self) -> str:
        self.insert_employee_sql = f"INSERT INTO employee (employeeid, firstname, lastname) VALUES ('{self.getEmployeeID()}', '{self.getFirstName()}', '{self.getLastName()}');"
        connect(self.insert_employee_sql)

    def show_employees(self) -> str:
        self.show_employee_sql = "SELECT * FROM employee;"
        connect(self.show_employee_sql)


def main():

    a = Employee(1337, "Peter", "Mustermann")
    print(sqlfunctions.insert_new_employee(a))
    sqlfunctions.show_employees(a)
    

if __name__ == '__main__':
    main()