from selenium.webdriver.support.ui import WebDriverWait


class BaseSwitch(object):

    def __get__(self, obj, owner):
        driver = obj.driver
        for handle in driver.window_handles:
            driver.switch_to.window(handle)

class SearchElement(object):
    def __init__(self, driver):
        self.driver = driver

    def set(self, locator, value):
        driver = self.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath(locator))
        driver.find_element_by_xpath(locator).send_keys(value)

    def get(self, locator):
        driver = self.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath(locator))
        driver.find_element_by_xpath(locator)

    def click(self, locator):
        driver = self.driver
        print(driver.find_element_by_xpath(locator))
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath(locator))
        driver.find_element_by_xpath(locator).click()
