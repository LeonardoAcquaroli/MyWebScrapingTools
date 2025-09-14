from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .driver import Driver

class BaseComponent:
    def __init__(self, driver):
        self.driver = driver

class Clicks(BaseComponent):
    def first_result_click(self, xpath='//*[@class="LC20lb MBeuO DKV0Md"]', timeout: float = 7):
        first = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        first.click()

    def nth_result_click(self, n: int, xpath='//*[@class="LC20lb MBeuO DKV0Md"]', timeout: float = 5):
        results = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath))
        )
        results[n-1].click()

    def click(self, xpath: str, timeout: float = 10):
        el = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        el.click()

class Elements(BaseComponent):
    def elements(self, xpath: str, timeout: float = 10, text: bool = False):
        elements = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath))
        )
        return [e.text for e in elements] if text else elements

    def element(self, xpath: str, timeout: float = 10, text: bool = False):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element.text if text else element

class Forms(BaseComponent):
    def login_form(self, xpath_user: str, username: str, xpath_password: str, password: str, xpath_login_button: str):
        user_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_user))
        )
        ActionChains(self.driver).send_keys_to_element(user_box, username).perform()

        password_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_password))
        )
        ActionChains(self.driver).send_keys_to_element(password_box, password).perform()

        login_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_login_button))
        )
        login_button.click()

    def cookies_handler(self, xpath: str, timeout: float = 3):
        btn = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        btn.click()

class Ladle:
    def __init__(self, headless: bool = True, log_level: int = 3, load_images: bool = False):
        driver_class = Driver()
        self.driver = driver_class.init_driver(headless=headless, log_level=log_level, load_images=load_images)

        # components that share the same driver
        self.clicks = Clicks(self.driver)
        self.elements = Elements(self.driver)
        self.forms = Forms(self.driver)

    def quit(self):
        try:
            self.driver.quit()
        except Exception:
            pass