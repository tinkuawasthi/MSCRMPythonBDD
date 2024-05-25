from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#from utilities.Commons import Commons


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.switch_to.default_content()

    def get_element(self, locator_type,locator_value):
        element = None
        self.is_element_clickable(locator_type,locator_value)
        if locator_type.endswith("_id"):
            element = self.driver.find_element(By.ID,locator_value)
        elif locator_type.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_type.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_type.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_type.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_type.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element

    def type_into_element(self, locator_type, locator_value, text):
        self.is_element_clickable(locator_type, locator_value)
        element = self.get_element(locator_type, locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def click_element(self, locator_type, locator_value):
        self.is_element_clickable(locator_type, locator_value)
        element = self.get_element(locator_type, locator_value)
        element.click()

    def is_element_clickable(self, locator_type, locator_value, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH,locator_value)))

    def is_element_displayed(self, locator_type, locator_value):
        return self.get_element(locator_type, locator_value).is_displayed()

    def is_element_text_contains(self,locator_type, locator_value,expected_text):
        element = self.get_element(locator_type, locator_value)
        print(element.text + "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print(expected_text)
        return element.text.__contains__(expected_text)

    def is_element_text_equals(self,locator_type, locator_value,expected_text):
        element = self.get_element(locator_type, locator_value)
        return element.text.__eq__(expected_text)
