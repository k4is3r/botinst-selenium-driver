from selenium import webdriver

#browser = webdriver.Chrome('/Users/k4is3r/Desktop/seleniumChrome/chromedriver')

class InstaBot:
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://instagram.com') 


if __name__ == '__main__':
    InstaBot()
