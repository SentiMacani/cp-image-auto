import base64
import io

import cv2
import numpy as np
from PIL import Image
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.constants import REFERENCE_WIDTH, REFERENCE_HEIGHT
from utils.execp_handler import *


## Image STuff

@signal_handling_wrapper
def find_image_in_screenshot(self, driver, target_img_path, threshold=0.7):
    self.driver = driver
    target_img = cv2.imread(target_img_path, 0)
    self.driver.update_settings({
        "getMatchedImageResult": True,
        "imageElementTapStrategy": "w3cActions",
        "imageMatchThreshold": 0.7,  # Lower threshold for more lenient matching
        "imageMatchMethod": "TM_CCOEFF_NORMED",
        "fixImageFindScreenshotDims": False,
        "fixImageTemplateSize": False,
        "autoUpdateImageElementPosition": True
    })
    screenshot_base64 = self.driver.get_screenshot_as_base64()
    screenshot_bytes = base64.b64decode(screenshot_base64)
    screenshot = Image.open(io.BytesIO(screenshot_bytes))
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)
    result = cv2.matchTemplate(screenshot, target_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= threshold:
        return (max_loc,
                (max_loc[0] + target_img.shape[1], max_loc[1] + target_img.shape[0]))
    else:
        return None

@signal_handling_wrapper
def take_screenshot_via_appium(self, driver):
    self.driver = driver
    
    self.driver.update_settings({
        "getMatchedImageResult": True,
        "imageElementTapStrategy": "w3cActions",
        "fixImageTemplateSize": False,
        "autoUpdateImageElementPosition": True
    })
    screenshot_base64 = self.driver.get_screenshot_as_base64()
    
    screenshot_bytes = base64.b64decode(screenshot_base64)
    
    
    return screenshot_bytes       


@signal_handling_wrapper
def click_image(self, driver, target_img_path, threshold=0.8, timeout=20):
    self.driver = driver
    start_time = time.time()
    while time.time() - start_time < timeout:
        result = find_image_in_screenshot(self, self.driver, target_img_path, threshold)
        if result:
            top_left, bottom_right = result
            center_x = (top_left[0] + bottom_right[0]) // 2
            center_y = (top_left[1] + bottom_right[1]) // 2
            tap(self, self.driver, center_x, center_y, 2)
            self.logger.info("CV2 - Clicked on image")
            return True
        safe_sleep(1)
    self.logger.info(f"CV2 - Image {target_img_path} is not present")
    return False


# Scaling Coords and Tap, Swipe, Scroll etc
@signal_handling_wrapper
def scale_coordinate(self, x, y):
    scaled_x = int(x * (self.screen_height / REFERENCE_HEIGHT))
    scaled_y = int(y * (self.screen_width / REFERENCE_WIDTH))
    return scaled_x, scaled_y


@signal_handling_wrapper
def tap(self, driver, x, y, z, tap_comments=None) -> None:
    self.driver = driver
    scaled_x, scaled_y = scale_coordinate(self, x, y)
    actions = ActionChains(self.driver)
    actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(scaled_x, scaled_y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    self.logger.info(f'Tap done, original coords {x}, {y} and new coords {scaled_x}, {scaled_y} {tap_comments}')
    safe_sleep(z)

@signal_handling_wrapper
def tap_non_scaled(self, driver, x, y, z, tap_comments=None) -> None:
    self.driver = driver
    
    actions = ActionChains(self.driver)
    actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(x, y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(0.1)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    self.logger.info(f'Tap done, original coords {x}, {y} and new coords {x}, {y} {tap_comments}')
    safe_sleep(z)    


@signal_handling_wrapper
def swipe(self, driver, x1, y1, x2, y2, z) -> None:
    self.driver = driver
    scaled_x1, scaled_y1 = scale_coordinate(self, x1, y1)
    scaled_x2, scaled_y2 = scale_coordinate(self, x2, y2)
    actions = ActionChains(self.driver)
    actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(scaled_x1, scaled_y1)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(scaled_x2, scaled_y2)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    self.logger.info('Swipe done')
    safe_sleep(z)


# i didnt integrate this to the above code because of that extra pause() function
@signal_handling_wrapper
def swipe_with_pause(self, driver, x1, y1, x2, y2, z) -> None:
    self.driver = driver
    scaled_x1, scaled_y1 = scale_coordinate(self, x1, y1)
    scaled_x2, scaled_y2 = scale_coordinate(self, x2, y2)
    actions = ActionChains(self.driver)
    try:
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(scaled_x1, scaled_y1)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(z / 1000)
        actions.w3c_actions.pointer_action.move_to_location(scaled_x2, scaled_y2)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        self.logger.info('Swipe done')
    except Exception as e:
        self.logger.info(e)


@signal_handling_wrapper
def click_using_image_recog(self, driver, img_path, timeout=5):
    self.driver = driver
    try:
        with open(img_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
        self.driver.update_settings({
            "getMatchedImageResult": True,
            "imageElementTapStrategy": "w3cActions",
            "imageMatchThreshold": 0.7,  # Lower threshold for more lenient matching
            "imageMatchMethod": "TM_CCOEFF_NORMED",
            "fixImageFindScreenshotDims": False,
            "fixImageTemplateSize": False,
            "autoUpdateImageElementPosition": True
        })
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((AppiumBy.IMAGE, encoded_image))).click()
        self.logger.info("Appium - Clicked on image")
        return True
    except Exception as e:
        self.logger.info(f"Appium - Image {img_path} is not present")
        return False


@signal_handling_wrapper
def is_present_image_recog(self, driver, img_path, timeout=5):
    self.driver = driver
    try:
        with open(img_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
        self.driver.update_settings({
            "getMatchedImageResult": True,
            "imageElementTapStrategy": "w3cActions",
            "imageMatchThreshold": 0.7,  # Adjust this value (0.1 to 1.0)
            "imageMatchMethod": "TM_CCOEFF_NORMED",  # Try different methods
            "fixImageTemplateSize": True,
            "fixImageFindScreenshotDims": False
        })
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((AppiumBy.IMAGE, encoded_image))
        )
        self.logger.info("Appium - Image is present")
        return True
    except Exception as e:
        self.logger.info(f"Appium - Image {img_path} is not present")
        return False
