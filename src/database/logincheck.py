import sys
sys.path.insert(0, "src//")
from database.dbconnect import DatabaseHandler

class Login(object):
    
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
        
        def userLogin2(self) -> bool:
            db = DatabaseHandler()
            query = f"select login('{self.getUsername()}','{self.getPassword()}')"
            return db.fetch_by_query(query)
            
                
def main():
    a = Login("malte@ist.cool","12345678")
    print(a.userlogin())
    print(a.userLogin2())
    
        
if __name__ == '__main__':
    main()
                
            
            