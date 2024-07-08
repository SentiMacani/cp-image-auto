import unittest
import asyncio
import time
from utils.android_actions import tap, is_present_image_recog, click_using_image_recog, click_image, take_screenshot_via_appium, tap_non_scaled
from utils.activity import save_activity_log
from utils.app_actions import login_using_key, input_name

import logging
from utils.setup_logger import logger
from utils.execp_handler import *
from faker import Faker

import threading
import pyautogui
import keyboard
from PIL import Image
from ultralytics import YOLO
import pydirectinput    
import time
import keyboard 
import io 


class Evermore_Nights_Loop_1(unittest.TestCase):
    
    def __init__(self, methodName='runTest', driver=None, login_key=None, username=None, pub_key=None, screen_width=None, screen_height=None, stop_flag=None):
        super().__init__(methodName)    
        self.driver = driver
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.username = username
        self.pub_key = pub_key
        self.login_key = login_key
        self.stop_flag = stop_flag
        self.logger = logging.getLogger('genleap_verbose')
    def run_bot(self,decision):
    
        if decision["login"]:
            print("login button has been found")
            center_x, center_y = decision["login-location"]
            print("location : " +str(decision["login-location"]))
            tap_non_scaled(self, self.driver, center_x, center_y, 2, "trying tap on login button via yolov8")
        elif decision["login-with-creoplay"]:
            print("login-with-creoplay has been found")
            # # keyboard.press("w")
            # # time.sleep(6)
            # # keyboard.release("w")
            # # keyboard.press("d")
            # # time.sleep(0.9)
            # # keyboard.release("d")
            # # keyboard.press("w")
            # # time.sleep(2)
            # # keyboard.release("w")
        elif decision["login-key"]:
            print("login-key found" + str(decision["login-key-location"]))

    def take_screenshot(self,stop_event, model):
        screenx_center = 1920/2
        screeny_center = 1080/2
        pyautogui.FAILSAFE = False

        while not stop_event.is_set():
            time.sleep(2)
            try:
                decision = {
                    "login": False,
                    "login-with-creoplay": False,
                    "login-key": False
                }

                # Take screenshot
                # screenshot = pyautogui.screenshot()
                # screenshot = Image.frombytes('RGB', screenshot.size, screenshot.tobytes())
                screenshot_bytes = take_screenshot_via_appium(self, self.driver )
                screenshot = Image.open(io.BytesIO(screenshot_bytes))
                
                #screenshot = Image.frombytes()
                
                results = model([screenshot], conf=.20)  # return a list of Results objects
                boxes = results[0].boxes.xyxy.tolist()
                classes = results[0].boxes.cls.tolist()
                names = results[0].names
                confidences = results[0].boxes.conf.tolist()

                # Process results list
                for box, cls, conf in zip(boxes, classes, confidences):
                    x1, y1, x2, y2 = box
                    
                    center_x = (x1+x2) / 2
                    center_y = (y1+y2) / 2

                    name = names[int(cls)]
                    
                    if name=="login":
                        print("login detected from screenshot with conf " + str(conf))
                        decision["login"] = True
                        decision["login-location"] = (center_x, center_y)
                    elif name == "login-with-creoplay" and conf>0.91:
                        print("login-with-creoplay detected from screnshot with conf " + str(conf))
                        decision["login-with-creoplay"] = True
                        decision["login-with-creoplay-location"] = (center_x, center_y)
                    elif name == "login-key":
                        print("login-key has been found with conf "+ str(conf))
                        decision["login-key"] = True
                        decision["login-key-location"] = (center_x, center_y)


            except Exception as e:
                print("exception raised" + e)
            
            self.run_bot(decision)
            


    @signal_handling_wrapper
    def test_loop_1(self):
        
        # Core test function code here
        # TODO @rahul write a new function which will try both appium and opencv2 \
        # simulatenously to find an image and if not found then skip  
             
        self.logger.info("Initialising")
        safe_sleep(3)

        #print(pyautogui.KEYBOARD_KEYS)
        model = YOLO('data/tutorialandlogin_v2.pt')
        stop_event = threading.Event()
        print("stop event set")
        
        # Create and start the screenshot thread
        screenshot_thread = threading.Thread(target=self.take_screenshot, args=(stop_event, model))
        screenshot_thread.start()
        print("thread started")

        # Listen for keyboard input to quit the program
        keyboard.wait("q")

        # Set the stop event to end the screenshot thread
        stop_event.set()

        # Wait for the screenshot thread to finish
        screenshot_thread.join()

        print("Program ended.")