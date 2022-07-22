import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import datetime
from time import sleep


COOKIE_URL = "https://orteil.dashnet.org/cookieclicker/"
LANGUAGE_SELECTION = "EN"
CHROME_DRIVER_PATH = "C:/Users/Quinn/Development/chromedriver.exe"
EXCEPTIONS = (selenium.common.exceptions.TimeoutException,
              selenium.common.exceptions.StaleElementReferenceException,
              selenium.common.exceptions.ElementClickInterceptedException)


class CookieBot:
    def __init__(self):
        self.driver = selenium.webdriver.Chrome(service=Service(executable_path=CHROME_DRIVER_PATH))
        self.game_player()

    def game_player(self):
        self.driver.get(url=COOKIE_URL)
        sleep(5)
        dismiss_cookies_button = self.waiter(By.XPATH, '/html/body/div[1]/div/a[1]', 10, "item")
        dismiss_cookies_button.click()
        language_option = self.driver.find_element(by=By.ID, value=f"langSelect-{LANGUAGE_SELECTION}")
        language_option.click()
        sleep(3)

        start_time = datetime.datetime.now()
        game_over_time = start_time + datetime.timedelta(minutes=5)

        while datetime.datetime.now() < game_over_time:
            self.shop_checker()
            self.upgrade_checker()
            next_update_time = datetime.datetime.now() + datetime.timedelta(seconds=5)

            while datetime.datetime.now() < next_update_time:
                big_cookie_button = self.waiter(By.ID, "bigCookie", 0.01, "item")
                big_cookie_button.click()

    def shop_checker(self):
        try:
            shop_item = self.waiter(By.CLASS_NAME, "crate.upgrade.enabled", 0.01, "item")
        except EXCEPTIONS:
            return
        else:
            shop_item.click()

    def upgrade_checker(self):
        try:
            upgrades = self.waiter(By.CLASS_NAME, "product.unlocked.enabled", 0.01, "list")
            upgrades[-1].click()
        except EXCEPTIONS:
            return
        else:
            self.upgrade_checker()

    def waiter(self, locate_by: By, value_to_locate: str, timeout: float, rtr_item_or_list: str):
        if rtr_item_or_list == "item":
            return WebDriverWait(driver=self.driver, timeout=timeout).until(
                expected_conditions.presence_of_element_located((locate_by, value_to_locate))
            )
        elif rtr_item_or_list == "list":
            return WebDriverWait(driver=self.driver, timeout=timeout).until(
                expected_conditions.presence_of_all_elements_located((locate_by, value_to_locate))
            )
