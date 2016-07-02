from selenium import webdriver
import time
import random as rand


class FirstSite(object):

    def __init__(self, ids=None):
        self.driver = webdriver.Firefox()
        if ids is None:
            self.ids = self.get_ids()
        else:
            self.ids = ids

    def get_url(id):
        """Return email form url for a given id number."""
        return "http://www.milanuncios.com/email/enviar-mensaje.php?id={}".format(id)

    def get_ids(self):
        """Go through the 'servicios' part of the site and record all user ids."""
        links = []
        first_site = "http://www.milanuncios.com/servicios/"
        self.driver.get(first_site)
        for x in range(199):
            x5_elements = self.driver.find_elements_by_class_name("x5")
            text = [i.text[1:] for i in x5_elements]
            links.append(text)
            try:
                next_button = self.driver.find_element_by_link_text("Siguiente")
                next_button.click()
            except:
                print x, "was the last page"
                break
        return map(str, links)


    def send_emails(self, name, email, text, number=""):
        """Send email for each id."""
        for id in self.ids:
            self.driver.get(get_url(id))

            form_name = self.driver.find_element_by_id("nombre")
            form_email = self.driver.find_element_by_id("email")
            form_number = self.driver.find_element_by_id("tfno")
            form_text = self.driver.find_element_by_id("mensaje")

            for letter in name:
                form_name.send_keys(letter)
                time.sleep(rand.random())
            for letter in email:
                form_email.send_keys(letter)
                time.sleep(rand.random())
            for letter in number:
                form_number.send_keys(letter)
                time.sleep(rand.random())
            for letter in text:
                form_text.send_keys(letter)
                time.sleep(rand.random())

            submit_button = self.driver.find_elements_by_class_name("btnsubmit")
            submit_button.click()

            time.sleep(rand.random() * 5)

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
