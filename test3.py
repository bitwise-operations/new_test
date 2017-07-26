#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from basic import Basic_settings
import page2
import time
from selenium.webdriver.common.keys import Keys

class Test_search(Basic_settings, unittest.TestCase):
    def __init__(self, *args, **kwargs):
        Basic_settings.__init__(self, *args, **kwargs)    
        unittest.TestCase.__init__(self, *args, **kwargs) 

    def test_seach(self):
        main_search = page2.MainSearch(self.driver, self.conf, self.base_url)
        main_search.search("S", self.pattern_search_form)
        main_search._click("search")
        time.sleep(3)
        

if __name__ == '__main__':
    unittest.main()