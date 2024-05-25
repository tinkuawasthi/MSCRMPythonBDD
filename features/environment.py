#hooks for creating setup and tear down for all scenarios
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

from utilities import ConfigReader


#hook methods for setu and tear down
def before_scenario(context, driver):
    browser_name = ConfigReader.read_configuration("basic_info", "browser")
    if browser_name.__eq__("chrome"):
        context.driver = webdriver.Chrome()
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.firefox()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.edge()
    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic_info", "url"))


def after_scenario(context,driver):
    context.driver.quit()


#save attachment on failures in step
def after_step(context,step):
    if step.status =='failed':
        allure.attach(context.driver.get_screenshot_as_png()
                      ,name="screenshot"
                      ,attachment_type = AttachmentType.PNG)

