import pytest
import unittest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.teststatus import TestStatus
from utilities import XLUtils
import time

@pytest.mark.usefixtures("oneTimeSetup")
class Test_002_DDT_Login():
    baseURL = ReadConfig.getApplicationURL()
    path = "./testData/LoginData.xlsx"
    logger = LogGen.loggen()  # Logger

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetup):
        self.driver=self.value
        self.ts = TestStatus()

    @pytest.mark.regression
    def test_login_ddt(self):
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        self.logger.info("******* Starting Test_002_DDT_Login Test **********")
        self.logger.info("******* Starting Login DDT Test **********")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        self.logger.info("******* Reading data from excel **********")
        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.status = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            if self.status == "True":
                if self.driver.title=="Dashboard / nopCommerce administration":
                    self.logger.info("Login Test Passed")
                    self.ts.mark("Pass", "Login Test Passed")
                    self.lp.clickLogout()
                else:
                    self.ts.mark("Fail", "Login Test Failed")
                    self.logger.info("Login Test Failed")

            elif self.status == "False":
                if self.driver.title!="Dashboard / nopCommerce administration":
                    self.ts.mark("Pass", "Login Test Passed")
                    self.logger.info("Login Test Passed")
                else:
                    self.ts.mark("Fail", "Login Test Failed")
                    self.logger.info("Login Test Failed")
                    self.lp.clickLogout()

        self.ts.markFinal("test_login_ddt", "Pass", "Login was successful")
        self.logger.info("******* Ending Login DDT Test **********")
        self.driver.close()
