from selenium import webdriver

#browser = webdriver.Chrome('/Users/k4is3r/Desktop/seleniumChrome/chromedriver')

class InstaBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--incognito')
        self.driver = webdriver.Chrome('./chromedriver',options=self.chrome_options)
        self.driver.get('https://instagram.com') 


if __name__ == '__main__':
    InstaBot()
