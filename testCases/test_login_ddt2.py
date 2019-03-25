import pytest
import unittest
import time
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures("oneTimeSetup")
class Test_003_DDT_Login(unittest.TestCase):
    baseURL = ReadConfig.getApplicationURL()

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetup):
        self.driver = self.value
        self.logger = LogGen.logger  # Logger
        self.ts = TestStatus()

    testdata = [
        ('admin@yourstore.com', 'admin', 'True'),
        ('admin@yourstore.com ', 'adm', 'False'),
        ('adm@yourstore.com', 'admin', 'False'),
        ('adm@yourstore.com', 'adm', 'False')]
    @pytest.mark.parametrize("user,password,status",testdata)
    def test_login_ddt2(self,user,password,status):
        self.logger.info("******* Starting Login Test **********")
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(user)
        self.lp.setPassword(password)
        self.lp.clickLogin()
        time.sleep(5)
        if status == "True":
            if self.driver.title == "Dashboard / nopCommerce administration":
                self.logger.info("Login Test Passed")
                self.ts.mark("Pass", "Login Test Passed")
                self.lp.clickLogout()
            else:
                self.ts.mark("Fail", "Login Test Failed")
                self.logger.info("Login Test Failed")

        elif status == "False":
            if self.driver.title != "Dashboard / nopCommerce administration":
                self.ts.mark("Pass", "Login Test Passed")
                self.logger.info("Login Test Passed")
            else:
                self.ts.mark("Fail", "Login Test Failed")
                self.logger.info("Login Test Failed")
                self.lp.clickLogout()

        self.ts.markFinal("test_login_ddt2", "Pass", "Login was successful")
        self.logger.info("******* Ending Login Test **********")
        self.driver.quit()
