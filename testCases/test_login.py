import pytest
import unittest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

@pytest.mark.usefixtures("oneTimeSetup")
class Test_001_Login():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetup):
        self.driver=self.value

    @pytest.mark.sanity
    def test_homePageTitle(self):
        self.logger.info("************* Test_001_Login **********")
        self.logger.info("******* Starting Home Page Title Test **********")
        self.driver.get(self.baseURL)

        if self.driver.title =="Your store. Login":
            assert True==True
            self.logger.info("HomePageTitle Test Passed")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_homePageTitle_scr.png")#Screenshot
            assert True == False
            self.logger.error("HomePageTitle Test Failed")

        self.driver.close()
        self.logger.info("******* Ending Home Page Title Test **********")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self):
        self.logger.info("******* Starting Login Test **********")
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        if self.driver.title=="Dashboard / nopCommerce administration":
            assert True==True
            self.logger.info("Login Test Passed")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login_scr.png")#Screenshot
            assert True == False
            self.logger.error("Login Test Failed")
        self.driver.close()
        self.logger.info("******* Ending Login Test **********")
