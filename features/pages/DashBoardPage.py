import time

from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage
from features.pages.NewCasePage import NewCasePage
from utilities import ConfigReader
#from utilities.Commons import Commons


class DashBoardPage(BasePage):

    #defining constructor for initializing the driver
    def __init__(self, driver):
        super().__init__(driver)
        #self.commons = Commons(self.driver)

    rms_App_Dashboard_Title_xpath = "//span[contains(.,'Customer Service Agent Dashboard')]"
    new_rms_case_option_xpath = "//div[@title='New Case Create']"


    def Is_DashBorad_Title_Present(self):
        self.is_element_clickable("rms_App_Dashboard_Title_xpath", self.rms_App_Dashboard_Title_xpath)
        return self.is_element_displayed("rms_App_Dashboard_Title_xpath", self.rms_App_Dashboard_Title_xpath)


    def click_create_new_case(self):
        self.is_element_clickable("new_rms_case_option_xpath", self.new_rms_case_option_xpath)
        self.click_element("new_rms_case_option_xpath", self.new_rms_case_option_xpath)
        return NewCasePage(self.driver)