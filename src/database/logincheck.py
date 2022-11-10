import sys
from dbconnect import DatabaseHandler

sys.path.insert(0, "src//")

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
            self.__logincheckingfunc = f"select login('{self.getUsername()}','{self.getPassword()}')"
            sqlpass.parser(self.__logincheckingfunc)
            self.logincheck = sqlpass.cur.fetchone()[0]
            return self.logincheck
                
def main():
    a = login("Peter@gmail.com","passwort123")
    print(a.userlogin())
    
        
    
    
                
if __name__ == '__main__':
    main()
                
            
            