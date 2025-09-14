from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import shutil
from typing import Union

class Driver():
    def __init__(self):
        pass

    def init_driver(self,
                    headless: bool = True,
                    log_level: Union[int, str] = 3,
                    load_images: bool = False,
                    language: str = None,
                    usear_agent_spoof: bool = True) -> webdriver.Chrome:
        # validate log_level
        allowed = {0, 1, 2, 3, "0", "1", "2", "3"}
        if log_level not in allowed:
            print(f"Invalid log_level {log_level}, setting to default (3).")
            log_level = 3

        # Options
        chrome_options = Options()
        if headless:
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--window-size=1600,1400')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-blink-features=AutomationControlled')
            chrome_options.add_argument('--disable-infobars')
        chrome_options.add_argument(f'log-level={log_level}')
        chrome_options.add_argument(f'--blink-settings=imagesEnabled={"true" if load_images else "false"}')
        chrome_options.add_argument(f'--lang={language}')
        # User-Agent spoof basico
        if usear_agent_spoof:
            chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0 Safari/537.36')

        driver = webdriver.Chrome(service=Service(self.get_chromedriver_path()), options=chrome_options)
        return driver

    def get_chromedriver_path(self):
        chromedriver_path = shutil.which("chromedriver")
        if chromedriver_path:
            return chromedriver_path
        # Auto download
        try:
            return ChromeDriverManager().install()
        except Exception as e:
            raise FileNotFoundError(f"Failed to locate or download chromedriver: {e}")