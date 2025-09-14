from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import shutil
from typing import List, Union

class Driver():
    def __init__(self):
        pass

    def init_driver(self,
                    headless: bool = True,
                    log_level: Union[int, str] = 3,
                    load_images: bool = False):
        # validate log_level
        allowed = {0, 1, 2, 3, "0", "1", "2", "3"}
        if log_level not in allowed:
            print(f"Invalid log_level {log_level}, setting to default (3).")
            log_level = 3

        # Options
        chrome_options = Options()
        if headless:
            chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'log-level={log_level}')
        chrome_options.add_argument(f'--blink-settings=imagesEnabled={"true" if load_images else "false"}')

        chrome_service = webdriver.ChromeService(executable_path=self.get_chromedriver_path())
        driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
        return driver

    def get_chromedriver_path(self):
        chromedriver_path = shutil.which("chromedriver")
        if chromedriver_path is None:
            raise FileNotFoundError("Chromedriver not found. Please ensure it is installed and in your system PATH.")
        return chromedriver_path