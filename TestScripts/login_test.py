import json

import pytest

from Pages.loginPage import loginPage

data_path = "D:\PythonLearning2025\MockData\LoginData.json"
with open(data_path) as f:
    test_data = json.load(f)  # Loads json data
    test_data_list = test_data["Users"]  # returns the Users dictionary data (list of users)


@pytest.mark.parametrize("test_data_items", test_data_list)
def test_valid_login(driver_instance, test_data_items):
    driver = driver_instance
    driver.get("https://practicetestautomation.com/practice-test-login/")

    login_page_obj = loginPage(driver)
    login_header = driver.find_element(*login_page_obj.lc_login_header)
    print(login_header.text)

    driver.find_element(*login_page_obj.lc_username_input).send_keys(test_data_items["Username"])
    driver.find_element(*login_page_obj.lc_password_input).send_keys(test_data_items["Password"])

    submit_btn = driver.find_element(*login_page_obj.lc_submit_btn)
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
    submit_btn.click()

    login_success_msg = driver.find_element(*login_page_obj.lc_login_successful_msg)
    assert login_success_msg.text == "Logged In Successfully", "Check User is logged in"
