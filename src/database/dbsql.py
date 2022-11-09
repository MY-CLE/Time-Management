from dbconnect import DatabaseHandler
<<<<<<< Updated upstream
import sys
sys.path.insert(0, "C:/Users/disga/Desktop/Studium SWB/SWB 3/Softwaretechnik/Labor/Waterfall STC/Softwaretechnik_2022/src/")
=======
sys.path.insert(0, "src//")
>>>>>>> Stashed changes
from components.stakeholder.Employee import Employee


class sqlfunctions(object):

    def insert_new_employee(self) -> str:
        sqlpass = DatabaseHandler()
        sqlpass.connect()
        self.insert_employee_sql = f"INSERT INTO employee (employeeid, firstname, lastname) VALUES ('{self.getEmployeeID()}', '{self.getFirstName()}', '{self.getLastName()}');"
        sqlpass.parser(self.insert_employee_sql)

    def show_employees() -> str:
        sqlpass = DatabaseHandler()
        sqlpass.connect()
        show_employee_sql = "SELECT DISTINCT * FROM employee WHERE firstname ='Peter';"
        sqlpass.parser(show_employee_sql)

def main():

    a = Employee(1337, "newtester", "Mustermann")
    #print(sqlfunctions.insert_new_employee(a))
    
    sqlfunctions.show_employees()
    #var = {"name": "hello"}
    #print(var["name"])

if __name__ == '__main__':
    main()