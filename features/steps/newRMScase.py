
from behave import *

from features.pages.DashBoardPage import DashBoardPage
from features.pages.LoginPage import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.NewCasePage import NewCasePage
from utilities import ConfigReader


# RMS Url https://ocrmstest.crm3.dynamics.com/


@given(u'I have logged into application')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.dashboard_page = context.login_page.login_To_Portal(ConfigReader.read_configuration("basic_info", "userName"),ConfigReader.read_configuration("basic_info", "passWord"))
    assert context.dashboard_page.Is_DashBorad_Title_Present()


@when(u'I click on New Case Creation button')
def step_impl(context):
    context.newCasePage = context.dashboard_page.click_create_new_case()



@then(u'New RMS Case creation page should be Opened for the User')
def step_impl(context):
    assert context.newCasePage.is_header_title_displayed()
