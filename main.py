from selenium import webdriver
from secrets import USERNAME,PW
import time 

class InstaBot:
    def __init__(self, username, pw):
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
if __name__ == '__main__':
    InstaBot(USERNAME,PW)
