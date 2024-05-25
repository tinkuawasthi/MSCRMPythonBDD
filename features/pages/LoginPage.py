import time

from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage
from features.pages.DashBoardPage import DashBoardPage
from utilities import ConfigReader
#from utilities.Commons import Commons


class LoginPage(BasePage):

    #defining constructor for initializing the driver
    def __init__(self,driver):
        super().__init__(driver)


    userName_input_xpath = "//input[@type='email']"
    passWord_input_xpath = "//input[@type='password']"
    next_button_xpath = "//input[@type='submit']"
    approve_request_text_xpath = "//div[@class='row text-title']"
    conformation_text_xpath = "//div[@id='idRichContext_DisplaySign']"
    oneCityRMS_app_xpath = "//div[@title='OneCity RMS - Officer App']"
    rms_App_Dashboard_Title_xpath = "//span[contains(.,'Customer Service Agent Dashboard')]"
    rms_officer_app_icon_xpath = "//iframe[@id='AppLandingPage']"

    def open_Login_Page(self):
        #self.commons = Commons(self.driver)
        self.driver.get(ConfigReader.read_configuration("basic_info", "url"))

    def type_UserName(self, userName):
        #element = self.get_element("userName_input_xpath",self.userName_input_xpath)
        #if element:
        self.type_into_element("userName_input_xpath",self.userName_input_xpath, userName)

    def type_PassWord(self, passWord):
        #element = self.get_element("passWord_input_xpath",self.passWord_input_xpath)
        #if element:
        self.type_into_element("passWord_input_xpath",self.passWord_input_xpath, passWord)
        #element.clear()
        #element.send_keys(passWord)
            #time.sleep(3)

    def click_Next_Submit_Button(self):
        self.driver.find_element(By.XPATH, self.next_button_xpath).click()

    def wait_for_approval(self):
        confirmation_text = self.is_element_clickable("approve_request_text_xpath",self.approve_request_text_xpath, 25)
        if confirmation_text != "":
            print(confirmation_text)  #self.commons.type_text(self.passWord_input_xpath, passWord)
            time.sleep(3)

    def wait_for_app_Icon(self):
        self.is_element_clickable("rms_officer_app_icon_xpath", self.rms_officer_app_icon_xpath, 25)
        time.sleep(5)

    def open_RMS_App(self):
        self.driver.switch_to.frame("AppLandingPage")
        elm = self.driver.find_element(By.XPATH, self.oneCityRMS_app_xpath)
        if elm:
            elm.click()
            #time.sleep(5)
            # back to default web page frame
        self.driver.switch_to.default_content()

        return DashBoardPage(self.driver)

    def login_To_Portal(self, username, password, dynamics=2):
        if dynamics == 2:
            self.type_UserName(username)
            self.click_Next_Submit_Button()
            self.type_PassWord(password)
            self.click_Next_Submit_Button()
            self.wait_for_approval()
            self.wait_for_app_Icon()
            return self.open_RMS_App()
            #self.click_element("rms_officer_app_icon_xpath",self.rms_officer_app_icon_xpath)
        else:
            self.type_UserName(username)
            self.type_PassWord(password)
            self.click_Next_Submit_Button()
