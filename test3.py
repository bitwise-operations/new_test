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
        
