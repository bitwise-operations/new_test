#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from basic import Basic_settings
import page2
import time
from selenium.webdriver.common.keys import Keys


class Test_form(Basic_settings, unittest.TestCase):
    def __init__(self, *args, **kwargs):
        Basic_settings.__init__(self, *args, **kwargs)    
        unittest.TestCase.__init__(self, *args, **kwargs) 

    def test_form(self):
        main_search = page2.MainSearch(self.driver, self.conf, self.base_url)
        main_search.lite_search(self.s_url, "Search_data_lite", self.pattern_search)
        # self.driver.get(self.base_url)
        self.driver.maximize_window()
        # main_search.cycle_for()
        main_search.search_element("Xpath_search", "get_results")
        time.sleep(1)
        main_search._click("thankyou")
        time.sleep(1)
        main_search._click("tour_1")
        main_search.switch_fr
        main_search._click("look_cost")
        time.sleep(3)
        main_search._click("package_1")
        time.sleep(2)
        main_search.switch_fr
        main_search.cycle_for("Buyer", self.pattern_form, "clientForm")
        main_search.cycle_for("Tourist1", self.pattern_form, "touristForm0")
        main_search.cycle_for("Tourist1", self.pattern_form, "touristForm1")
        main_search._click("contract")
        main_search._click("book_tour")
        time.sleep(10)
        url = self.driver.current_url
        print(url)



if __name__ == '__main__':
    unittest.main()