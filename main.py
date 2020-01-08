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
        time.sleep(5)
        self.driver.find_element_by_xpath('//a[contains(@href, "/{}/following/")]'\
                   .format(self.username)).click()
        following = self._get_names()

        self.driver.find_element_by_xpath('//a[contains(@href, "/{}/followers/")]'\
                   .format(self.username)).click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        followers_count = len(followers)
        following_count = len(following)
        not_following_back_count = len(not_following_back)
        print(f'You have {followers_count} followers in {self.username} account')
        print(f'You are following {following_count} users in {self.username} account')
        print(f'The users that not following you are {not_following_back_count} users')
        print('This is the list of users are note following you')
        for user in not_following_back:
            print(f' User: {user}')
        self.driver.quit()



    def _get_names(self):
        #sugs =self.driver.find_element_by_xpath('//h4[contains(text(),Suggestions)]')
        time.sleep(5)
        #self.driver.execute_scripts('arguments[0].scrollIntoView()',sugs)
        scroll_box = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
        last_h, ht = 0, 1
        while last_h != ht:
            last_h = ht
            time.sleep(3)
            ht = self.driver.execute_script("""
                 arguments[0].scrollTo(0, arguments[0].scrollHeight);
                 return arguments[0].scrollHeight;
                 """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        #print(names)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()
        return names

if __name__ == '__main__':
    my_bot = InstaBot(USERNAME,PW)
    my_bot.get_unfollowers()
