#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import configparser
from os import path


class Configs:
    def __init__(self, *args, **kwargs):
        pass

    def configs(self):
        self.conf = configparser.RawConfigParser()
        self.conf.read(path.abspath('./_configs/text.ini'))
        self.base_url = self.conf.get("Url", "base_url")
        self.s_url = self.conf.get("Url", "s_url")
        self.pattern_form = self.conf.get("Xpath_field", "pattern_form")
        self.pattern_search = self.conf.get("Url", "pattern_search")
        