from selenium import webdriver
import time
import random as rand


class SecondSite(object):

    def __init__(self):
        self.driver = webdriver.Firefox()
        self._get_settings()
        self.driver.get("http://www.tusclasesparticulares.com/")

    def _get_settings(self):
        self.driver.set_window_size(960, 540)
        self.driver.set_window_position(0, 540)

    def click_buscar(self):
        self.driver.find_element_by_id("buscar").click()

    def find_links(self):
        links = self.driver.find_elements_by_class_name("titanuncio")
        return links

    def click_next(self):
        next_button = self.driver.find_element_by_link_text("Siguiente")
        next_button.click()

    def enter_personal_info(self, name, email):
        form_name = self.driver.find_element_by_id("txtname")
        form_email = self.driver.find_element_by_id("txtmail")
        for letter in name:
            form_name.send_keys(letter)
            time.sleep(rand.random())
        for letter in email:
            form_email.send_keys(letter)
            time.sleep(rand.random())

    def enter_text(self, text):
        form_text = self.driver.find_element_by_id("txttext")
        form_text.clear()
        for letter in text:
            form_text.send_keys(letter)
            time.sleep(rand.random())

    def click_submit(self):
        submit_button = self.driver.find_element_by_id("btnenviar")
        submit_button.click()

    def click_back(self):
        self.driver.back()

    def click_next(self):
        next_button = self.driver.find_element_by_link_text("Siguiente")
        next_button.click()
