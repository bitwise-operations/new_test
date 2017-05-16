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
        self.country = self.conf.get("Search_data", "country")
        self.nights = self.conf.get("Search_data", "nights")
        self.adult = self.conf.get("Search_data", "adult")
        self.departure_city = self.conf.get("Search_data", "departure_city")
        self.s_url = self.conf.get("Url", "s_url")
        self.pattern_form = self.conf.get("Xpath_field", "pattern_form")
        