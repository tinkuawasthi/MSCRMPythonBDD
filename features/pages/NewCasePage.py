import time

from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage
from utilities import ConfigReader
#from utilities.Commons import Commons


class NewCasePage(BasePage):

    #defining constructor for initializing the driver
    def __init__(self, driver):
        super().__init__(driver)
        #self.commons = Commons(self.driver)

    new_case_header_title_xpath = "//h1[@data-id='header_title']"

    def is_header_title_displayed(self):
        self.is_element_clickable("new_case_header_title_xpath",self.new_case_header_title_xpath)
        return self.is_element_displayed("new_case_header_title_xpath",self.new_case_header_title_xpath)
