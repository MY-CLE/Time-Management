class Employee(object):

    def __init__(self, employeeID: int, firstName: str, lastName: str):
        self.__employeeID = employeeID
        self.__firstName = firstName
        self.__lastName = lastName

    def getEmployeeID(self) -> int:
        return self.__employeeID

    def getFirstName(self) -> str:
        return self.__firstName

    def getLastName(self) -> str:
        return self.__lastName

