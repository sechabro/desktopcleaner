from selenium import webdriver
from selenium.webdriver.common.by import By


def get_access_token(auth_url=None):
    driver = webdriver.Safari()
    driver.get(auth_url)
    print(auth_url)
    driver.implicitly_wait(2)
    continue_button = driver.find_element(
        by=By.ID, value="warning-button-continue")
    continue_button.click()
    driver.implicitly_wait(2)
    allow_button = driver.find_element(
        by=By.CLASS_NAME, value="dig-Button dig-Button--primary dig-Button--large auth-button auth-button-allow")
    allow_button.click()
    driver.implicitly_wait(2)
    access_code_element = driver.find_element(
        by=By.ID, value="auth-code-input")
    access_code = access_code_element.value
