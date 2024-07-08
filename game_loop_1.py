import unittest
import asyncio
import time
from utils.android_actions import tap, is_present_image_recog, click_using_image_recog, click_image
from utils.activity import save_activity_log
from utils.app_actions import login_using_key, input_name

import logging
from utils.setup_logger import logger
from utils.execp_handler import *
from faker import Faker


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


    @signal_handling_wrapper
    def test_loop_1(self):
        
        # Core test function code here
        # TODO @rahul write a new function which will try both appium and opencv2 \
        # simulatenously to find an image and if not found then skip  
             
        self.logger.info("Initialising")
        safe_sleep(56)

        #TODO @rahul add check for updates - download conditional loop

        tap(self, self.driver, 2099, 881, 2, "Log out an existing user")
        tap(self, self.driver, 1230, 885, 5, "Log In")
        tap(self, self.driver, 1220, 405, 6, "Log In")
        login_using_key(self, self.driver, self.login_key)
        safe_sleep(15)
        
        if click_image(self, self.driver, "images/Privacypolicy-itel.jpg", 0.8, 5) or \
            is_present_image_recog(self, self.driver, "images/Privacypolicy.jpg", 2) or  \
            is_present_image_recog(self, self.driver, "images/Privacypolicy-itel.jpg", 5):
            tap(self, self.driver, 609, 841, 0.7, "Privacy Policy Step Try 2")
            tap(self, self.driver, 977, 841, 0.7, "Privacy Policy Step Try 2")
            tap(self, self.driver, 1712, 850, 2.7, "Privacy Policy Step Try 2")

        tap(self, self.driver, 1280, 790, 13, "Privacy Policy Steps over")
        # #TODO improve this condition by adding unique itel specific images for det
        if is_present_image_recog(self, self.driver, "images/Tutorialscreen.jpg") or \
            click_image(self, self.driver, "images/Tutorialscreen.jpg", 0.8, 5):
            # For Initial Gameplay Only
            for x in range(4):
                tap(self, self.driver, 1895, 210, 2, "tap to fast forward")
            # faker = Faker()
            input_name(self, self.driver, self.username)
            save_activity_log(self, self.pub_key+'&'+self.username, 'bind_creoplay', 'activity')
            tap(self, self.driver, 2197, 70, 2)
            tap(self, self.driver, 1359, 676, 20, "dialogue skipped")
            for x in range(5):
                tap(self, self.driver, 1895, 210, 4, "tap to fast forward")
            tap(self, self.driver, 2197, 70, 2)
            tap(self, self.driver, 1359, 676, 6, "dialogue skipped")
            tap(self, self.driver, 1920, 536, 8, "move clicked")
            tap(self, self.driver, 1895, 210, 2, "tap to fast forward")
            tap(self, self.driver, 1770, 996, 2)
            tap(self, self.driver, 1544, 642, 5, "attacking enemy")
            tap(self, self.driver, 1895, 210, 2, "tap to fast forward")
            tap(self, self.driver, 2240, 988, 2)
            tap(self, self.driver, 1878, 712, 11, "attacking enemy")
            tap(self, self.driver, 1921, 538, 8, "move clicked")
            tap(self, self.driver, 1770, 996, 2)
            tap(self, self.driver, 1889, 631, 9, "attacking boss enemy")
            for x in range(7):
                tap(self, self.driver, 1895, 210, 1, "tap to fast forward")
            safe_sleep(2)
            tap(self, self.driver, 2197, 70, 2)
            tap(self, self.driver, 1359, 676, 10, "dialogue skipped")
            tap(self, self.driver, 2130, 938, 3, "confirm")
            tap(self, self.driver, 2136, 941, 2, "next stage")
            #first adventure battle
            tap(self, self.driver, 2102, 954, 13, "battle")
            tap(self, self.driver, 2197, 70, 2)
            tap(self, self.driver, 1359, 676, 6, "dialogue skipped")
            tap(self, self.driver, 1923, 539, 8, "move clicked")
            for x in range(7):
                tap(self, self.driver, 1895, 210, 2, "tap to fast forward")
            tap(self, self.driver, 1767, 993, 2)
            tap(self, self.driver, 1618, 673, 12, "attacking enemy")
            tap(self, self.driver, 1895, 210, 1, "tap to fast forward")
            tap(self, self.driver, 1767, 993, 2)
            tap(self, self.driver, 1901, 743, 14, "tap to fast forward")
            for x in range(2):
                tap(self, self.driver, 1895, 210, 3, "tap to fast forward")
            tap(self, self.driver, 1916, 990, 2)
            tap(self, self.driver, 1618, 673, 12, "attacking enemy")
            tap(self, self.driver, 1895, 210, 1, "tap to fast forward")
            tap(self, self.driver, 1767, 993, 1)
            tap(self, self.driver, 1901, 743, 12, "attacking enemy")
            if is_present_image_recog(self, self.driver, "images/battleicon2.jpg", 2) or \
                click_image(self, self.driver, "images/battleicon3.jpg", 0.8, 2) or \
                is_present_image_recog(self, self.driver, "images/battleicon3.jpg", 2):
                tap(self, self.driver, 1767, 993, 1)
                tap(self, self.driver, 1618, 673, 8, "attacking enemy")
                tap(self, self.driver, 1767, 993, 1)
                tap(self, self.driver, 1901, 743, 1, "attacking enemy")
            # donotremove
            safe_sleep(8)
            tap(self, self.driver, 1923, 539, 8, "move clicked")
            tap(self, self.driver, 1767, 993, 1)
            tap(self, self.driver, 1843, 686, 8, "attacking boss enemy")
            tap(self, self.driver, 1767, 993, 1)
            tap(self, self.driver, 1843, 686, 8, "attacking boss enemy")
            tap(self, self.driver, 1767, 993, 1)
            tap(self, self.driver, 1843, 686, 10, "attacking boss enemy")
            if is_present_image_recog(self, self.driver, "images/Slimeboss.jpg", 2) or \
                click_image(self, self.driver, "images/Slimeboss.jpg", 0.8, 2) or \
                is_present_image_recog(self, self.driver, "images/battleicon3.jpg", 2):
                tap(self, self.driver, 1767, 993, 1)
                tap(self, self.driver, 1843, 686, 8, "attacking boss enemy")
            tap(self, self.driver, 2197, 70, 2)
            tap(self, self.driver, 1359, 676, 12, "dialogue skipped")
            tap(self, self.driver, 2130, 938, 3, "confirm")
            tap(self, self.driver, 2136, 941, 3, "next stage")
            tap(self, self.driver, 2102, 954, 12, "battle")
            tap(self, self.driver, 2197, 70, 2)
            tap(self, self.driver, 1359, 676, 6, "dialogue skipped")
            tap(self, self.driver, 1923, 539, 8, "move clicked")
            for x in range(4):
                tap(self, self.driver, 1895, 210, 3, "tap to fast forward")
            tap(self, self.driver, 1767, 993, 1)
            tap(self, self.driver, 1843, 686, 8, "attacking enemy")
            tap(self, self.driver, 1767, 993, 1)
            tap(self, self.driver, 1843, 686, 8, "attacking enemy")
            tap(self, self.driver, 1767, 993, 1)
            tap(self, self.driver, 1728, 780, 8, "attacking enemy")
            tap(self, self.driver, 1767, 993, 1)
            tap(self, self.driver, 1728, 780, 8, "attacking enemy")
            if is_present_image_recog(self, self.driver, "images/battleicon2.jpg", 2) or \
                click_image(self, self.driver, "images/battleicon3.jpg", 0.8, 2) or \
                is_present_image_recog(self, self.driver, "images/battleicon3.jpg", 2):
                tap(self, self.driver, 1767, 993, 1)
                tap(self, self.driver, 1566, 686, 8, "attacking enemy")
                tap(self, self.driver, 1767, 993, 1)
                tap(self, self.driver, 1901, 780, 8, "attacking enemy")
            tap(self, self.driver, 1923, 539, 8, "move clicked")
            tap(self, self.driver, 1767, 993, 1)
            tap(self, self.driver, 1843, 686, 8, "attacking boss enemy")
            tap(self, self.driver, 1767, 993, 1)
            tap(self, self.driver, 1843, 686, 10, "attacking boss enemy")
            if is_present_image_recog(self, self.driver, "images/Slimeboss.jpg", 2) or \
                click_image(self, self.driver, "images/Slimeboss.jpg", 0.8, 2) or \
                is_present_image_recog(self, self.driver, "images/battleicon3.jpg", 2):
                tap(self, self.driver, 1767, 993, 1)
                tap(self, self.driver, 1843, 686, 8, "attacking boss enemy")
                tap(self, self.driver, 1767, 993, 1)
                tap(self, self.driver, 1843, 686, 8, "attacking boss enemy")
            tap(self, self.driver, 2197, 70, 2)
            tap(self, self.driver, 1359, 676, 12, "dialogue skipped")
            tap(self, self.driver, 2130, 938, 6, "confirm")
            tap(self, self.driver, 2136, 941, 4, "next")
            tap(self, self.driver, 2102, 954, 13, "battle")
            for x in range(3):
                tap(self, self.driver, 1895, 210, 2, "tap to fast forward")
            tap(self, self.driver, 2197, 70, 2)
            tap(self, self.driver, 1359, 676, 15, "dialogue skipped")
            tap(self, self.driver, 2264, 37, 7, "home")
            for x in range(6):
                tap(self, self.driver, 1895, 210, 3, "tap to fast forward")
            tap(self, self.driver, 1932, 539, 1)
            tap(self, self.driver, 1880, 168, 3)
            tap(self, self.driver, 1895, 210, 2)
            tap(self, self.driver, 195, 972, 2)
            tap(self, self.driver, 186, 725, 4)
            tap(self, self.driver, 533, 442, 2)
            for x in range(4):
                tap(self, self.driver, 1895, 210, 1, "tap to fast forward")
            tap(self, self.driver, 1932, 539, 1)
            tap(self, self.driver, 1932, 539, 1)
            tap(self, self.driver, 1932, 539, 1)
            tap(self, self.driver, 1880, 168, 1)
            tap(self, self.driver, 2264, 37, 5)
            for x in range(17):
                tap(self, self.driver, 1895, 210, 1, "tap to fast forward")
            tap(self, self.driver, 707, 969, 5)
            tap(self, self.driver, 1932, 539, 1)
            tap(self, self.driver, 1880, 168, 1)
            tap(self, self.driver, 168, 49, 3)
            for x in range(7):
                tap(self, self.driver, 1895, 210, 3, "tap to fast forward")
            # donotremove
            safe_sleep(2)
            tap(self, self.driver, 2200, 948, 2)
            for x in range(3):
                tap(self, self.driver, 1895, 210, 1, "tap to fast forward")
            tap(self, self.driver, 1140, 844, 2)
            tap(self, self.driver, 2078, 963, 2)
            for x in range(8):
                tap(self, self.driver, 1895, 210, 1, "tap to fast forward")
            tap(self, self.driver, 1932, 539, 1)
            tap(self, self.driver, 1880, 168, 1)
            tap(self, self.driver, 2264, 37, 5)

        # /For Initial Gameplay Only
        safe_sleep(18)
        if is_present_image_recog(self, self.driver, "images/Dailylogin.jpg", 6) or \
                click_image(self, self.driver, "images/Dailylogin.jpg"):
            for x in range(3):
                tap(self, self.driver, 1801, 926, 2)
            save_activity_log(self, self.pub_key+'&'+self.username, 'daily_login_claim', 'activity')
            for x in range(5):
                tap(self, self.driver, 972, 82, 1)

        # ADVENTURE BATTLE

        # Battling and to win Twice
        tap(self, self.driver, 2200, 948, 2, "Adventure clicked")
        tap(self, self.driver, 289, 289, 1)
        tap(self, self.driver, 289, 289, 2)
        tap(self, self.driver, 220, 198, 2, "team 1 clicked")
        tap(self, self.driver, 2084, 957, 12, "BATTLE clicked")
        save_activity_log(self, self.pub_key+'&'+self.username, 'use_stamina', 'activity')
        tap(self, self.driver, 2179, 64, 15, "AUTOMATE clicked")
        safe_sleep(45)
        # tap(self, self.driver, 2190, 68, 58, "Automate button Clicked")
        tap(self, self.driver, 1895, 210, 2, "random click")
        tap(self, self.driver, 2130, 951, 2, "confirm click")
        save_activity_log(self, self.pub_key+'&'+self.username, 'adventure', 'battle')
        tap(self, self.driver, 2130, 951, 5, "nextstage click")
        tap(self, self.driver, 2084, 957, 60, "battle clicked")
        save_activity_log(self, self.pub_key+'&'+self.username, 'use_stamina', 'activity')
        tap(self, self.driver, 1895, 210, 2, "random click")
        tap(self, self.driver, 2133, 948, 5, "confirm click")
        save_activity_log(self, self.pub_key+'&'+self.username, 'adventure', 'battle')
        # tap(self, self.driver, 2084, 957, 3, "Next Stage Clicked")
        tap(self, self.driver, 2264, 37, 10, "We are going back to home page")

        # /Battling and to win Twice
        # Golden CHalice Summon
        tap(self, self.driver, 878, 972, 8)
        tap(self, self.driver, 283, 457, 2)
        tap(self, self.driver, 1688, 960, 10)
        tap(self, self.driver, 2185, 85, 10)
        tap(self, self.driver, 1423, 966, 10)
        save_activity_log(self, self.pub_key+'&'+self.username, 'gacha', 'activity')
        tap(self, self.driver, 174, 49, 10)

        # self.driver.terminate_app('com.nomina.evermoreknights')
        # self.driver.quit()