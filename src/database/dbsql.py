import sys
from dbconnect import DatabaseHandler

sys.path.insert(0, "src//")
from components.stakeholder.Employee import Employee


class sqlfunctions(object):

    def insert_new_employee(self) -> str:
        sqlpass = DatabaseHandler()
        sqlpass.connect()
        self.insert_employee_sql = f"INSERT INTO employee (employeeid, firstname, lastname) VALUES ('{self.getEmployeeID()}', '{self.getFirstName()}', '{self.getLastName()}');"
        sqlpass.parser(self.insert_employee_sql)

    def show_employees(self) -> str:
        sqlpass = DatabaseHandler()
        sqlpass.connect()
        self.show_employee_sql = "SELECT * FROM employee;"
        sqlpass.parser(self.show_employee_sql)


def main():

    a = Employee(1337, "tester", "Mustermann")
    print(sqlfunctions.insert_new_employee(a))
    
    #sqlfunctions.show_employees(a)
    

if __name__ == '__main__':
    main()