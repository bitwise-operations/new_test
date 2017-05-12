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

    def lite_search(self, s_url, section):
        driver = self.driver
        departure_city = self.conf.get(section, "departure_city")
        country = self.conf.get(section, "country")
        date_depart = self.conf.get(section, "date_depart")
        nights = self.conf.get(section, "nights")
        adult = self.conf.get(section, "adult")
        kids = self.conf.get(section, "kids")

        data = "-".join([departure_city, "to", country, "departure", date_depart, "for", nights, "nights", adult, "adults", kids, "kids-1..5-stars"])
        _url = "/".join([self.base_url, s_url, data])
        driver.get(_url)

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
