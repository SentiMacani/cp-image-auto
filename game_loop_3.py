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


class Evermore_Nights_Loop_3(unittest.TestCase):
    
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
    def test_loop_3(self):
        
        # Core test function code here
        # TODO @rahul write a new function which will try both appium and opencv2 \
        # simulatenously to find an image and if not found then skip
        
        # self.driver = webdriver.Remote(appium_server_url, options=AppiumOptions().load_capabilities(capabilities))
           
        self.logger.info("Initialising gameloop_3")
        # safe_sleep(56)

        #TODO @rahul add check for updates - download conditional loop

        # tap(self, self.driver, 2099, 881, 2, "Log out an existing user")
        # tap(self, self.driver, 1230, 885, 5, "Log In")
        # tap(self, self.driver, 1220, 405, 8, "Log In")
        # login_using_key(self, self.driver, self.login_key)
        # safe_sleep(5)
        
        # if click_image(self, self.driver, "images/Privacypolicy-itel.jpg", 0.8, 5) or \
        #     is_present_image_recog(self, self.driver, "images/Privacypolicy.jpg", 1) or  \
        #     is_present_image_recog(self, self.driver, "images/Privacypolicy-itel.jpg", 1):
        #     tap(self, self.driver, 612, 841, 0.7)
        #     tap(self, self.driver, 977, 841, 0.7)
        #     tap(self, self.driver, 1712, 850, 2.7, "accept clicked")

        # tap(self, self.driver, 1280, 790, 12, "Tap to Start clicked")

        # /For Initial Gameplay Only
        # safe_sleep(20)
        # if is_present_image_recog(self, self.driver, "images/Dailylogin.jpg", 2) or \
        #         click_image(self, self.driver, "images/Dailylogin.jpg", 0.8, 2):
        #     for x in range(3):
        #         tap(self, self.driver, 1801, 926, 2)
        #     for x in range(5):
        #         tap(self, self.driver, 972, 82, 1)

        # ADVENTURE BATTLE

       # Adventure
        safe_sleep(10)
        tap(self, self.driver, 2200, 948, 5, "Adventure clicked")
        tap(self, self.driver, 289, 289, 3, "act1-1 clicked")
        tap(self, self.driver, 289, 289, 4, "act1-1 clicked")
        tap(self, self.driver, 220, 198, 4, "team 1 clicked")
        tap(self, self.driver, 2084, 957, 13, "battle 1 clicked")
        save_activity_log(self, self.pub_key+'&'+self.username, 'use_stamina', 'activity')
        # tap(self, self.driver, 2179, 64, 1, "Automate button Clicked")

        # MISSING: Speed button clicks
        # HIGHLIGHT START
        tap(self, self.driver, 2096, 61, 1)
        tap(self, self.driver, 2096, 61, 1, "Speed button Clicked")
        safe_sleep(40)
        # HIGHLIGHT END

        # repeat battle
        tap(self, self.driver, 1895, 210, 2)
        tap(self, self.driver, 2133, 948, 2, "Confirm Clicked")
        save_activity_log(self, self.pub_key+'&'+self.username, 'adventure', 'battle')
        tap(self, self.driver, 2145, 945, 5)
        tap(self, self.driver, 2084, 957, 2, "battle 2 clicked")
        save_activity_log(self, self.pub_key+'&'+self.username, 'use_stamina', 'activity')
        safe_sleep(52)

        # repeat battle
        tap(self, self.driver, 1895, 210, 2)
        tap(self, self.driver, 2133, 948, 2, "Confirm Clicked")
        save_activity_log(self, self.pub_key+'&'+self.username, 'adventure', 'battle')
        tap(self, self.driver, 2145, 945, 5)
        tap(self, self.driver, 2084, 957, 20, "battle(cutscene) clicked")
        save_activity_log(self, self.pub_key+'&'+self.username, 'use_stamina', 'activity')
        
        # next stage
        tap(self, self.driver, 2197, 70, 2)
        tap(self, self.driver, 1359, 676, 12)
        tap(self, self.driver, 1146, 826, 2, "act1-4 clicked")
        tap(self, self.driver, 1146, 826, 2, "act1-4 clicked")
        tap(self, self.driver, 220, 198, 2, "team 1 clicked")
        tap(self, self.driver, 2084, 957, 12, "battle 3 clicked")
        save_activity_log(self, self.pub_key+'&'+self.username, 'use_stamina', 'activity')
        
        safe_sleep(122)
        
        # # MISSING: Additional skip check
        # # HIGHLIGHT START
        # if is_present_image_recog(self, self.driver, "images/Skip.jpg"):
        #     tap(self, self.driver, 2197, 70, 2, "skip clicked")
        #     tap(self, self.driver, 1359, 676, 10, "yes clicked")
        # # HIGHLIGHT END
        
        # safe_sleep(40)
        # if is_present_image_recog(self, self.driver, "images/Skip.jpg"):
        #     tap(self, self.driver, 2197, 70, 2, "skip clicked")
        #     tap(self, self.driver, 1359, 676, 10, "yes clicked")

        # repeat battle
        tap(self, self.driver, 1895, 210, 2)
        tap(self, self.driver, 2133, 948, 2, "Confirm Clicked")
        save_activity_log(self, self.pub_key+'&'+self.username, 'adventure', 'battle')
        tap(self, self.driver, 2145, 945, 5)
        tap(self, self.driver, 2084, 957, 2, "battle 4 clicked")
        save_activity_log(self, self.pub_key+'&'+self.username, 'use_stamina', 'activity')
        safe_sleep(320)
        #safe_sleep(120)

        # # repeat battle
        # tap(self, self.driver, 1895, 210, 2)
        # tap(self, self.driver, 2133, 948, 2, "confirm Clicked")
        # asyncio.run(save_activity_log(self, self.pub_key+'&'+self.username, 'adventure', 'battle'))
        # tap(self, self.driver, 2145, 945, 5)
        # tap(self, self.driver, 2084, 957, 2, "battle clicked")
        # asyncio.run(save_activity_log(self, self.pub_key+'&'+self.username, 'use_stamina', 'activity'))
        # safe_sleep(120)
        
        # # repeat battle
        # tap(self, self.driver, 1895, 210, 2, "random touch to fast forward")
        # tap(self, self.driver, 2133, 948, 2, "confirm button Clicked")
        # asyncio.run(save_activity_log(self, self.pub_key+'&'+self.username, 'adventure', 'battle'))
        # tap(self, self.driver, 2145, 945, 5, "next stage button Clicked")
        # tap(self, self.driver, 2084, 957, 2, "battle clicked")
        # asyncio.run(save_activity_log(self, self.pub_key+'&'+self.username, 'use_stamina', 'activity'))
        # safe_sleep(120)
        
        # # repeat battle
        # tap(self, self.driver, 1895, 210, 2, "random touch to fast forward")
        # tap(self, self.driver, 2133, 948, 2, "confirm button Clicked")
        # asyncio.run(save_activity_log(self, self.pub_key+'&'+self.username, 'adventure', 'battle'))
        # tap(self, self.driver, 2145, 945, 5, "next stage button Clicked")
        # tap(self, self.driver, 2084, 957, 2, "battle clicked")
        # asyncio.run(save_activity_log(self, self.pub_key+'&'+self.username, 'use_stamina', 'activity'))
        # safe_sleep(120)

        # next stage
        tap(self, self.driver, 1895, 210, 2, "random touch to fast forward")
        tap(self, self.driver, 2133, 948, 5, "confirm button Clicked")
        save_activity_log(self, self.pub_key+'&'+self.username, 'adventure', 'battle')
        tap(self, self.driver, 2264, 37, 10, "home button Clicked")
        safe_sleep(20)

        # MISSING: Golden Chalice Summon
        # HIGHLIGHT START
        tap(self, self.driver, 878, 969, 8, "summon button Clicked")
        tap(self, self.driver, 283, 457, 2, "Golden Chalice Clicked")
        tap(self, self.driver, 1688, 960, 10, "summon x 1 button Clicked")
        save_activity_log(self, self.pub_key+'&'+self.username, 'gacha', 'activity')
        tap(self, self.driver, 2185, 85, 3, "skip button Clicked")
        tap(self, self.driver, 999, 969, 10, "summon x 1 button Clicked")
        save_activity_log(self, self.pub_key+'&'+self.username, 'spend_zenny', 'activity')
        save_activity_log(self, self.pub_key+'&'+self.username, 'gacha', 'activity')
        tap(self, self.driver, 2185, 85, 3, "skip button Clicked")
        tap(self, self.driver, 1423, 966, 10, "confirm button Clicked")
        tap(self, self.driver, 174, 49, 10, "GOLDEN CHALICE SUMMON DONE")
        # HIGHLIGHT END

        # MISSING: Daily Mission Claim
        # HIGHLIGHT START
        tap(self, self.driver, 1045, 969, 4, "missions button Clicked")
        tap(self, self.driver, 1840, 966, 10, "Claim all Clicked")
        save_activity_log(self, self.pub_key+'&'+self.username, 'daily_mission', 'activity')
        tap(self, self.driver, 515, 372, 3, "chest 1 Clicked")
        tap(self, self.driver, 856, 935, 1, "random Click")
        tap(self, self.driver, 640, 372, 3, "chest 2 Clicked")
        tap(self, self.driver, 856, 935, 1, "random Click")
        tap(self, self.driver, 2264, 37, 10, "home button Clicked")
        # HIGHLIGHT END

        # MISSING: Terminate app
        # HIGHLIGHT START
        self.driver.terminate_app('com.nomina.evermoreknights')