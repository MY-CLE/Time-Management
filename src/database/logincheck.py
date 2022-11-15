import sys
sys.path.insert(0, "src//")
from database.dbconnect import DatabaseHandler
import re
class Login(object):
    
        logincheck = False
        
        def __init__(self, email:str, password:str):
            if (email == '') or (password == ''):
                raise ValueError
            
            filter_email = re.compile(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")
            if filter_email.findall(email) == []:
                raise ValueError

            self.__email = email
            self.__password = password

                
        def getPassword(self) -> str:
            return self.__password
        
        def getEmail(self) -> str:
            return self.__email

        def userlogin(self) -> bool:
            sqlpass = DatabaseHandler()
            
            #add sql logic
            
            #example
            #self.__login_attempt = f"SELECT email,password FROM employee WHERE email={self.getEmail()} AND password={self.getPassword()}"
            self.__logincheckingfunc = f"SELECT login('{self.getEmail()}','{self.getPassword()}')"
            return sqlpass.parser(self.__logincheckingfunc)[0][0]
        
        def userLogin2(self) -> bool:
            db = DatabaseHandler()
            query = f"SELECT login('{self.getEmail()}','{self.getPassword()}')"
            return db.parser(query)
            
                
def main():
    a = Login("malte@ist.cool","12345678")
    print(a.userlogin())
    print(a.userLogin2())
    
        
if __name__ == '__main__':
    main()
                
            
            