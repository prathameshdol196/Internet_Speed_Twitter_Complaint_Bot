
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

CHROME_DRIVER_PATH = "YOUR CHROME DRIVER PATH"
PROMISED_DOWN = 1
PROMISED_UP = 1
TWITTER_EMAIL = "TWITTER EMAIL ID"
TWITTER_PASSWORD = "TWITTER PASSWORD"
USER_ID = "TWITTER USER ID"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.current_up = 0
        self.current_down = 0

    def get_internet_speed(self):  # this function gets internet speed
        self.driver.get("https://www.speedtest.net/")  # website to test internet speed
        sleep(5)  # sleep until data is loaded
        self.go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        # ^ click on the go GO button to test internet speed

        sleep(50)
        self.current_down = float(self.driver.find_element(By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        # ^ getting current download speed

        self.current_up = float(self.driver.find_element(By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)
        # ^ getting current upload speed

    def tweet_at_provider(self):  # this function tweets to isp
        self.driver.get("https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoiZW4ifQ%3D%3D%22%7D")
        # ^ twitter link
        sleep(10)

        if self.current_down < PROMISED_DOWN or self.current_up < PROMISED_UP:

            user_name = self.driver.find_element(By.XPATH,
                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
            user_name.click()
            user_name.send_keys(TWITTER_EMAIL)
            sleep(1)
            user_name.send_keys(Keys.ENTER)
            sleep(2)
            # ^ twitter username

            sleep(2)
            password = self.driver.find_element(By.XPATH,
                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(TWITTER_PASSWORD)
            sleep(1)
            password.send_keys(Keys.ENTER)
            sleep(2)
            # ^ twitter password

            sleep(5)
            compose_tweet = self.driver.find_element(By.XPATH,
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
            sleep(2)
            compose_tweet.click()
            sleep(2)
            tweet = f"Hey Internet Provider, why is my internet speed {self.current_down}down/{self.current_up}up which is less than {PROMISED_DOWN}down/{PROMISED_UP}up"
            compose_tweet.send_keys(tweet)
            # ^ compose tweet

            print(f"Hey Internet Provider, why is my internet speed {self.current_down}down/{self.current_up}up which is less than {PROMISED_DOWN}down/{PROMISED_UP}up")
        else:
            print("your internet speed is good")


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

