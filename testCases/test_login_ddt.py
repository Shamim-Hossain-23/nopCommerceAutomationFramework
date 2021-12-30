import time

import pytest
from selenium import webdriver
from webdriver_manager import driver
from pageObject.Login_page import LoginPage
from utilities.ReadProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:

    base_url = ReadConfig.getApplicationUrl()
    log = LogGen.custom_logger()
    path = ".//TestData/LoginData.xlsx"

    def test_logIn_ddt(self, setup):
        self.log.info("************************ Test_002_DDT_Login ****************************")
        self.log.info("************************ Verify Login DDT Test ****************************")

        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in excel", self.rows)
        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.log.info("********** Pass ***********")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.log.info("********** Fail *************")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.log.info("********** Fail ***********")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.log.info("********** Pass *************")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.log.info("*********Login DDT test is Passed ***********")
            self.driver.close()
            assert True
        else:
            self.log.info("*********Login DDT test is Failed ***********")
            self.driver.close()
            assert False

        self.log.info("******* End of Login DDT Test **********")
        self.log.info("**************** Completed  TC_LoginDDT_002 ************* ")




