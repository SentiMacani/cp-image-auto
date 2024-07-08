from appium.webdriver.common.appiumby import AppiumBy
import faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from utils.android_actions import *
from utils.execp_handler import *

# elements
game_view_screen = (AppiumBy.XPATH, '//android.view.View[@content-desc="Game view"]')
play_store_close_button = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Not Now"]')
login_key_tab = (AppiumBy.XPATH, '//android.view.View[@text="Login Key"]')
login_key_input = (AppiumBy.XPATH, '//android.widget.EditText')
login_button = (AppiumBy.XPATH, '//android.widget.Button[@text="Login"]')
name_input = (AppiumBy.CLASS_NAME, 'android.widget.EditText')
name_ok_button = (AppiumBy.XPATH, '//android.widget.Button[@text="OK"]')

@signal_handling_wrapper
def click_game_view(self, driver) -> None:
    self.driver = driver
    WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable(game_view_screen)) \
        .click()
    safe_sleep(30)

@signal_handling_wrapper
def close_play_store(self, driver) -> None:
    self.driver = driver
    WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable(play_store_close_button)) \
        .click()
    safe_sleep(2)

@signal_handling_wrapper
def login_using_key(self, driver, login_key, max_retries=5):
    self.driver = driver
    
    def find_and_interact(locator, action, input_text=None):
        for attempt in range(max_retries):
            try:
                element = WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located(locator)
                )
                if action == "click":
                    element.click()
                elif action == "send_keys":
                    element.clear()
                    element.send_keys(input_text)
                return True
            except (StaleElementReferenceException, TimeoutException, NoSuchElementException) as e:
                self.logger.error(f"Attempt {attempt + 1} failed: {str(e)}")
                if attempt == max_retries - 1:
                    self.logger.error(f"Failed to interact with {locator} after {max_retries} attempts")
                    return False
                safe_sleep(1)  # Short pause before retrying
        return False
    
    for attempt in range(max_retries):
        try:
            # Click login key tab
            if not find_and_interact(login_key_tab, "click"):
                raise Exception("Failed to click login key tab")

            # Input login key
            if not find_and_interact(login_key_input, "send_keys", login_key):
                raise Exception("Failed to input login key")

            swipe_with_pause(self, self.driver, 1859, 954, 1859, 0, 30)
            safe_sleep(1)

            # Click login button
            if not find_and_interact(login_button, "click"):
                raise Exception("Failed to click login button")

            safe_sleep(5)
            self.logger.info('Login successful')
            return True
        except Exception as e:
            self.logger.error(f"Login attempt {attempt + 1} failed: {str(e)}")
            if attempt == max_retries - 1:
                self.logger.error(f"Login failed after {max_retries} attempts")
                return False
            safe_sleep(2)  # Short pause before retrying the whole login process
    
    return False

# todo retry logic is not working here - need to fix
@signal_handling_wrapper
def input_name(self, driver, name, max_retries=5):
    self.driver = driver

    def find_and_interact(locator, action, input_text="Geneleap"):
        for attempt in range(max_retries):
            try:
                element = WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located(locator)
                )
                if action == "click":
                    element.click()
                elif action == "send_keys":
                    element.clear()
                    element.send_keys(input_text)
                return True
            except StaleElementReferenceException:
                if attempt == max_retries - 1:
                    self.logger.error(f"StaleElementReferenceException: Failed to interact with {locator}")
                    return False
            except TimeoutException:
                self.logger.error(f"TimeoutException: Element not found {locator}")
                return False

    try:
        # Input name
        if not find_and_interact(name_input, "send_keys", name):
            raise Exception("Failed to input name")

        safe_sleep(2)  # Short pause after entering name

        # Click OK button
        if not find_and_interact(name_ok_button, "click"):
            raise Exception("Failed to click OK button")

        safe_sleep(3)  # Wait for the action to complete
        self.logger.info(f'Name "{name}" entered successfully')
        return True
    except Exception as e:
        self.logger.error(f"Failed to input name: {str(e)}")
        return False