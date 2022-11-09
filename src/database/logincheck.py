import sys
from dbconnect import DatabaseHandler

sys.path.insert(0, "src//")
from components.stakeholder.Employee import Employee

class login(object):
    
        logincheck = False;
        
        def __init__(self, username:str, password:str):
                self.__username = username
                self.__password = password
                
        def getPassword(self) -> str:
            return self.__password
        
        def getUsername(self) -> str:
            return self.__username

        def userlogin(self) -> bool:
            sqlpass = DatabaseHandler()
            sqlpass.connect()
            
            #add sql logic
            
            #example
            #self.__login_attempt = f"SELECT username,password FROM employee WHERE username={self.getUsername()} AND password={self.getPassword()}"
            self.__logincheckingfunc = f"EXEC login({self.getUsername()},{self.getPassword()}"
            self.logincheck = sqlpass.parser(self.__logincheckingfunc)
            return self.logincheck
                
def main():
    a = login("Peter","passwort123")
    #if a.userlogin() == True:
        
    
    
                
if __name__ == '__main__':
    main()
                
            
            