from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
import time


def get_auth_code(auth_url=None):
    options = webdriver.ChromeOptions()
    chrome_profile = "/Users/seanbrown/Library/Application\ Support/Google/Chrome/"
    user_data = "Profile 1"
    options.add_argument(f"--user-data-dir={chrome_profile}")
    options.add_argument(f"--profile-directory={user_data}")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(auth_url)
    time.sleep(3)
    code = auth_code(driver=driver)
    return code


def dbox_login(driver=None):
    '''in case login needs to occur beforehand, this can be
    worked into the flow. current automation
    relies on session info from chrome profile.'''
    driver.get("https://www.dropbox.com/login")
    email_input = driver.find_element(
        by=By.NAME, value="progressive_susi_email")
    driver.implicitly_wait(3)
    ActionChains(driver).send_keys_to_element(
        email_input, "email_here").perform()
    return_key = Keys.RETURN
    ActionChains(driver).send_keys_to_element(
        email_input, return_key).perform()
    time.sleep(3)
    password_input = driver.find_element(
        by=By.NAME, value="login_password")
    ActionChains(driver).send_keys_to_element(
        password_input, "password_here").perform()
    print('found it')
    ActionChains(driver).send_keys_to_element(
        password_input, return_key).perform()
    time.sleep(5)
    return


def auth_code(driver=None):
    time.sleep(3)
    continue_button = driver.find_element(
        by=By.ID, value="warning-button-continue")
    ActionChains(driver).click(continue_button).perform()
    time.sleep(2)
    ActionChains(driver).click(continue_button).perform()
    time.sleep(2)
    allow_button = driver.find_element(
        by=By.CSS_SELECTOR, value="#auth > div.auth-buttons-container > button.dig-Button.dig-Button--primary.dig-Button--large.auth-button.auth-button-allow")
    ActionChains(driver).click(allow_button).perform()
    time.sleep(2)
    auth_code_element = driver.find_element(by=By.ID, value="auth-code-input")
    auth_code = auth_code_element.get_attribute("value")
    return auth_code
