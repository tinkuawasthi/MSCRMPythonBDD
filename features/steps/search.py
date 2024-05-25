from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By



@given(u'I got navigated to Home page')
def step_impl(context):
    context.driver.get("https://tutorialsninja.com/demo/")


@when(u'I entered valid product into Search box field')
def step_impl(context):
    context.driver.find_element(By.NAME,"search").send_keys("HP")


@when(u'I click on Search button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@id='search']//button").click()


@then(u'Valid product should be displayed in Search results')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()


@when(u'I entered invalid product into Search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("Honda")


@then(u'Proper message should be displayed in Search results')
def step_impl(context):
    expected_text = "There is no product that matches the search criteria."
    assert context.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p")\
        .text.__eq__(expected_text)


@when(u'I do not enter value into Search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("")
