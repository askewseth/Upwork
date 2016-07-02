import time
import random as rand
from tusclases_sender import SecondSite



def main():
    d = SecondSite()
    time.sleep(rand.random() * 6)
    d.click_buscar()
    time.sleep(rand.random() * 4)
    d.click_next()
    links_initial = d.find_links()
    for i, _ in enumerate(links_initial):
        links = d.find_links()
        links[i].click()
        time.sleep(rand.random() * 15)
        try:
            d.enter_personal_info("Seth", "sethsemailscraper@gmail.com")
            time.sleep(rand.random() * 5)
        except:
            pass
        d.enter_text("Hello! I was wondering if you" +
                     " by change taught spanish lessons?")
        time.sleep(rand.random() * 3)
        d.click_submit()
        time.sleep(rand.random() * 5)
        d.click_back()
        d.click_back()
        time.sleep(rand.random() * 3)


if __name__ == "__main__":
    main()
