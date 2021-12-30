import pytest
from selenium import webdriver
from webdriver_manager import driver
from pageObject.Login_page import LoginPage
from utilities.ReadProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:

    base_url = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    log = LogGen.custom_logger()

    @pytest.mark.regression
    def testHomPageTitle(self, setup):
        self.log.info("************************ Test_001_Login ****************************")
        self.log.info("******************** Verify Home Page Title ************************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        # Validation
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.log.info("************************ Home Page Title Test is Passed ****************************")

        else:
            self.driver.save_screenshot(".\\Screensorts\\"+"testHomePageTitle.png")
            self.driver.close()
            self.log.error("************************ Home Page Title Test is Failed ****************************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def testLogIn(self, setup):
        self.log.info("************************ Verify Login Test ****************************")

        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        # validation
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.log.info("************************ Login Test is Passed ****************************")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screensorts\\"+"testLogIn.png")
            self.driver.close()
            self.log.error("************************ Login Test is Failed ****************************")
            assert False



