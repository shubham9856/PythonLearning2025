from selenium.webdriver.common.by import By

from Utilities.BrowserUtilities import BrowserUtilities


class loginPage(BrowserUtilities):
    def __init__(self, driver):
        super().__init__(self)
        self.driver = driver

        self.lc_login_header = (By.XPATH, '//h2[text()="Test login"]')
        self.lc_username_input = (By.ID, 'username')
        self.lc_password_input = (By.ID, 'password')
        self.lc_submit_btn = (By.ID, 'submit')

        self.lc_login_successful_msg = (By.XPATH, '//h1[text()="Logged In Successfully"]')
