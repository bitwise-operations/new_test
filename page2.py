from element import BaseSwitch
from element import SearchElement
import time
import re


class Switch(BaseSwitch):
    pass


class BasePage(object):

    def __init__(self, driver, conf=None, base_url=None):
        self.driver = driver
        self.conf = conf
        self.base_url = base_url


class MainSearch(BasePage):
    switch_fr = BaseSwitch()

    def search(self, section, location):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        # self.cycle_for()
        # {}
        # m[k]=x
        a = self.data_search(section)
        s = SearchElement(self.driver)
        try:
            a['country']
            s.set(location.format("1", "/input"), a['country'])
        except KeyError:
            pass
        try:
            a['date_depart']
            info = s.get(location.format("2", "/div/span"))
            date_def = re.findall(r'[0-9]{1,2}', info.text)
            value = int(date_def[0])

            # s.set(location.format("2"))
        except KeyError:
            pass
        try:
            a['nights']
            info = s.get(location.format("3", "//span"))
            value = int(re.findall(r'[0-9]{1,2}', info.text)[0])
            s.click(location.format("3", "/div"))
            vol_fill = int(a['nights'])
            i = 0
            if value > vol_fill:
                for i in range(value - vol_fill):
                    s.click(location.format("3", "//div[@class='subtract']"))
            elif value < vol_fill:
                for i in range(vol_fill - value):
                    s.click(location.format("3", "//div[@class='add']"))
            else:
                pass
        except KeyError:
            pass
        try:
            a['adult']
            info = s.get(location.format("4", "/div"))
            value = int(re.findall(r'[0-9]{1}', info.text)[0])
            s.click(location.format("4", "/div"))
            vol_fill = int(a['adult'])
            i = 0
            if value > vol_fill:
                for i in range(value - vol_fill):
                    s.click(location.format("4", "//div[@class='subtract']"))
            elif value < vol_fill:
                for i in range(vol_fill - value):
                    s.click(location.format("4", "//div[@class='add']"))
            else:
                pass
        except KeyError:
            pass
        try:
            a['kids']
            s.click(location.format("4", "/div"))
            s.click(location.format("4", "//select"))
            kids = a['kids'].split(',')
            i = 0
            for i in range(len(kids)):
                s.click(location.format("4", "//select/option[@value='" + kids[i] + "']"))
        except KeyError:
            pass
        try:
            a['departure']
            s.click(location.format("5", "/input"))
            s.set(location.format("5", "/input"), a['departure'])
        except KeyError:
            pass

        # получаем из конфига список значений
        # затем проверяем какие из параметров по умолчанию нужно заменить

    def data_search(self, section):
        key_lst = [option for option in self.conf[section]]
        value_lst = [value for value in self.conf[section].values()]
        my_dict = dict(zip(key_lst, value_lst))

        return my_dict

    def filler_form(self):
        len(driver.find_elements_by_css_selector(".tourists_list > div"))

    def lite_search(self, s_url, section, pattern):
        driver = self.driver
        values = [value for value in self.conf[section].values()]
        url = pattern.format(self.base_url, s_url, *values)
        driver.get(url)
        driver.maximize_window()

    def _click(self, name_button, section="Xpath_buttton"):
        xpath = self.conf.get(section, name_button)
        s = SearchElement(self.driver)
        s.click(xpath)

    def data_entry(self, section, option, name_field,
                   section_field="Xpath_field"):
        value = self.conf.get(section, option)
        locator = self.conf.get(section_field, name_field)
        s = SearchElement(self.driver)
        s.set(locator, value)

    def search_element(self, section, option):
        locator = self.conf.get(section, option)
        s = SearchElement(self.driver)
        s.get(locator)

    def cycle_for(self, section, xpath_form, id_form):
        s = SearchElement(self.driver)
        a = [option for option in self.conf[section]]
        for i in range(len(a)):
            value = self.conf.get(section, a[i])
            locator = xpath_form.format(id_form, a[i])
            s.set(locator, value)
            time.sleep(2)
