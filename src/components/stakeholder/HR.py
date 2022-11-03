from Employee import *


class HR(Employee):
    def __init__(self, employeeID: int, firstName: str, lastName: str):
        super().__init__(employeeID, firstName, lastName)
