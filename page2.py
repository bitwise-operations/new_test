from element import BaseSwitch
from element import SearchElement
import time


class Switch(BaseSwitch):
    pass

class BasePage(object):

    def __init__(self, driver, conf=None, base_url=None):
        self.driver = driver
        self.conf = conf
        self.base_url = base_url

class MainSearch(BasePage):
    switch_fr = BaseSwitch()

    def search(self, section):
        # driver = self.driver
        # driver.get(self.base_url)
        # driver.maximize_window()
        # self.cycle_for()
        # {}
        # m[k]=x
        a = self.data_search(section)

        try:
            a['country']
        except KeyError:
            pass
        try:
            a['date_depart']
        except KeyError:
            pass
        try:
            a['nights']
        except KeyError:
            pass
        try:
            a['adult']
        except KeyError:
            pass
        try:
            a['kids']
        except KeyError:
            pass
        try:
            a['departure']
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

    def data_entry(self, section, option, name_field, section_field="Xpath_field"):
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
