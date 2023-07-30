from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains


def get_auth_code(auth_url=None):
    driver = webdriver.Safari()
    driver.get(auth_url)
    print(auth_url)
    driver.implicitly_wait(8)
    print(driver.current_url)
    dbox_login(driver=driver)
    return auth_code(driver=driver)


def dbox_login(driver=None):
    driver.get("https://www.dropbox.com/login")
    email_input = driver.find_element(
        by=By.NAME, value="progressive_susi_email")
    driver.implicitly_wait(3)
    ActionChains(driver).send_keys_to_element(
        email_input, "********").perform()
    return_key = Keys.RETURN
    ActionChains(driver).send_keys_to_element(
        email_input, return_key).perform()
    driver.implicitly_wait(3)

    # password not inputting. need to fix
    password_input = driver.find_element(
        by=By.NAME, value="login_password")
    ActionChains(driver).send_keys_to_element(
        password_input, "********").perform()
    # driver.implicitly_wait(3)
    # ActionChains(driver).send_keys_to_element(
    #    password_input, return_key).perform()
    driver.implicitly_wait(3)
    return


def auth_code(driver=None):
    continue_button = driver.find_element(
        by=By.ID, value="warning-button-continue")
    continue_button.click()
    driver.implicitly_wait(2)
    allow_button = driver.find_element(
        by=By.CLASS_NAME, value="dig-Button dig-Button--primary dig-Button--large auth-button auth-button-allow")
    allow_button.click()
    driver.implicitly_wait(2)
    auth_code_element = driver.find_element(
        by=By.ID, value="auth-code-input")
    auth_code = auth_code_element.value
    return auth_code
