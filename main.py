from selenium import webdriver
from secrets import USERNAME,PW
import time 

class InstaBot:
    def __init__(self, username, pw):
        self.username = username
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--incognito')
        self.driver = webdriver.Chrome('./chromedriver',options=self.chrome_options)
        self.driver.get('https://instagram.com')
        time.sleep(5)
        self.driver.find_element_by_xpath('//a[contains(text(), "Inicia sesión")]').click()
        time.sleep(5) 
        self.driver.find_element_by_xpath('//input[@name=\'username\']').send_keys(username)
        self.driver.find_element_by_xpath('//input[@name=\'password\']').send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        time.sleep(10)
        self.driver.find_element_by_xpath('//button[contains(text(),"Ahora no")]').click()
        time.sleep(6)
        
            
    def get_unfollowers(self):
        self.driver.find_element_by_xpath('//a[contains(@href,"/{}")]'.format(self.username)).click()
        self.driver.find_element_by_xpath('//a[contains(@href, "/seguidores")]')\
                   .click()
        sugs =self.driver.find_element_by_xpath('//h4[contains(text(),Suggestions)]')
        self.driver.execute_scripts('arguments[0].scrollIntoView()',sugs)
        scroll_box = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]')
        last_h, ht = 0, 1
        while last_h != ht:
            last_h = ht
            time.sleep(3)
            ht = self.driver.execute_scripts("""
                 arguments[0].scrollTo(0, arguments[0].scrollHeight);
                 return arguments[0].scrollHeight;
                 """, scroll_box)


if __name__ == '__main__':
    my_bot = InstaBot(USERNAME,PW)
