from selenium import webdriver


class Screenshot:
    def __init__(self, url):
        self.url = url

    def load(self):
        browser = webdriver.Chrome(executable_path="/Users/adrian/Downloads/chromedriver")
        browser.get(self.url)
        browser.get_screenshot_as_file('screenshot.png')


pic = Screenshot("https://mastery.games/")
pic.load()
