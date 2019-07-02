from selenium import webdriver


class Screenshot:
    def __init__(self, browser):
        self.browser = browser

    def take_screenshot(self):
        sc = self.browser
        sc.maximize_window()
        sc.get("https://mastery.games/")
        sc.save_screenshot("screenshot.png")


if __name__ == "__main__":
    pic = Screenshot(webdriver.Chrome(executable_path="/Users/adrian/Downloads/chromedriver"))
    pic.take_screenshot()
