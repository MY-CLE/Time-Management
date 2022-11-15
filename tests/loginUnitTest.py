import sys
import unittest
sys.path.insert(0, "src//")
import database.logincheck as lgn


class LoginUnitTest(unittest.TestCase):
    
    def test_normal_input(self):
        """
        Test if the return functions work
        """
        login = lgn.Login('bob.andews@mail.com', 'diedrei???')
        self.assertEqual('bob.andews@mail.com', login.getEmail()) 
        self.assertEqual('diedrei???',login.getPassword())
    
    def test_no_input(self):
        """
        If there are no User inputs assert error
        """
        #login = lgn.Login()
        with self.assertRaises(ValueError):
            lgn.Login('','')
            
    def test_wrong_email(self):
        '''
        Raise error when not a real email adress as input
        '''
        emailList = ['@', '4', 'bob@andrews@mail.com', 'Ralph', '175824312', 'bob andrews@mail.de' ]
        
        for email in emailList:
            with self.assertRaises(ValueError):
                login = lgn.Login(email,'diedrei???')
                                
    def test_db_return_value(self):
        login = lgn.Login('bob.andrews@mail.com', 'diedrei???')
        self.assertEqual(login.userlogin(),True)
        
            



if __name__ == '__main__':
    unittest.main()
