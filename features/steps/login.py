#minimize lines of code here. move things as much to do it.
#creation of pageobject should be a part of calling function to optimize code.


from behave import *

from features.pages.DashBoardPage import DashBoardPage
from features.pages.LoginPage import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities import ConfigReader


# RMS Url https://ocrmstest.crm3.dynamics.com/


@given(u'I navigate to Login Page')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open_Login_Page()

    #assert context.driver.title.__eq__(exp_title)


@when(u'I entered valid UserName as "{userName}"')
def step_impl(context, userName):
    context.login_page.type_UserName(userName)
    context.login_page.click_Next_Submit_Button()
    #print("Inside : - ")


@when(u'I entered valid Password as "{passWord}"')
def step_impl(context, passWord):
    context.login_page.type_PassWord(ConfigReader.read_configuration("basic_info", "passWord"))
    #context.login_page.click_Next_Submit_Button()

    print("Inside : - ")


@when(u'I click on Login button')
def step_impl(context):
    expected_text = "Customer Service Agent Dashboard"
    context.login_page.click_Next_Submit_Button()
    context.login_page.wait_for_approval()
    context.login_page.wait_for_app_Icon()
    context.dashboard_page = context.login_page.open_RMS_App()
    #asserting the return value of function to Tru or false
    assert context.dashboard_page.Is_DashBorad_Title_Present()


@then(u'App should be Opened for User')
def step_impl(context):
    print("Inside : - ")


@when(u'I entered invalid UserName')
def step_impl(context):
    print("Inside : - ")


@then(u'I should get a proper warning message')
def step_impl(context):
    print("Inside : - ")


@when(u'I entered invalid Password')
def step_impl(context):
    print("Inside : - ")


@when(u'I do not enter any value in UserName and Password')
def step_impl(context):
    print("Inside : - ")
