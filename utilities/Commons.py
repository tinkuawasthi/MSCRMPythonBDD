"""from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Commons:
    # defining constructor for initializing the driver
    def __init__(self, driver):
        self.driver = driver

    def get_element(self,locator):
        self.is_element_clickable(locator)
        return self.driver.find_element(By.XPATH,locator)

    def type_text(self,locator,text):
        self.is_element_clickable(locator)
        self.driver.find_element(By.XPATH,locator).send_keys(text)

    def click_element(self,locator):
        self.is_element_clickable(locator)
        self.driver.find_element(By.XPATH,locator).click()

    def is_element_clickable(self, locator, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH,locator)))

    def is_element_displayed(self, locator):
        return self.driver.find_element(By.XPATH, locator).is_displayed()"""


