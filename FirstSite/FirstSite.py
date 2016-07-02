from selenium import webdriver
import time
import random as rand

class Driver(object):

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.home_window = None
        self.driver.get("http://www.milanuncios.com/servicios/")

    def get_home_window(self):
        self.home_window = self.driver.current_window_handle

    def get_links(self, link_text):
        links = self.driver.find_elements_by_partial_link_text(link_text)
        return links

    def get_source(self):
        source = self.driver.page_source
        return source

    def switch_active(self):
        self.driver.switch_to_active_element()

    def switch_back(self):
        if self.window_home is not None:
            driver.switch_to_window(self.home_window)
        else:
            raise Exception("Driver home window was never defined")


def main():
    d = Driver()
    links = d.get_links()
