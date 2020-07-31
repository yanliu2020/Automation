# -*- coding:utf-8 -*-
from configparser import ConfigParser
from selenium import webdriver
from pageobjects.login.login import SystemLogin
from config.login.login_entity import  LoginEntity
from utils.basepath_helper import logs_path, project_path, drivers_path, config_path,utils_path
from utils.logger import logger
from utils.base_page import BasePage

class BrowserEngine(object):
    chrome_driver_path = drivers_path + 'chromedriver.exe'
    firefox_driver_path = drivers_path + 'geckodriver.exe'
    ie_driver_path = drivers_path + 'IEDriverServer.exe'
    edge_driver_path = 'C:\\Windows\\SysWOW64\\MicrosoftWebDriver.exe'
    geckodriver_path = utils_path + 'geckodriver.log'

    def __init__(self):
        self.driver = None

    def open_browser(self):
        config = ConfigParser()
        file_path = config_path + 'config.ini'
        config.read(file_path)

        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")
        logger.info("The test server url is: %s" % url)

        if browser == "Firefox":
            profile = webdriver.FirefoxProfile()
            profile.set_preference('browser.download.dir', project_path)
            profile.set_preference('browser.download.folderList', 2)
            profile.set_preference('browser.download.manager.showWhenStarting', False)
            profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/x-octetstream')
            #self.driver = webdriver.Firefox(firefox_profile=profile, executable_path=self.firefox_driver_path,log_path=r'E:\Automation\UI\utils\geckodriver.log')
            self.driver = webdriver.Firefox(firefox_profile=profile, executable_path=self.firefox_driver_path,
                                            log_path=self.geckodriver_path)
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            self.driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            self.driver = webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser.")
        elif browser == "Edge":
            self.driver = webdriver.Edge(self.edge_driver_path)
            logger.info("Starting Edge browser.")

        self.driver.maximize_window()
        """
        # 云服务器默认屏幕分辨率1024*768，此分辨率下无法正常执行
        # 后续增加对屏幕分辨率进行判断，以适应不同分辨率下的测试执行
        """
        #self.driver.set_window_size(1920, 1080)
        logger.info("Maximize the current window.")

        self.driver.get(url)
        logger.info("Open url: %s" % url)

        # self.driver.implicitly_wait(3)
        # logger.info("Set implicitly wait 10 seconds.")

        BasePage(self.driver).find_element_by_wait('xpath',LoginEntity.login_title)

        #传入登陆用户名和密码
        SystemLogin(self.driver).user_login('yan.liu@an-chen.com','Lychan@2012')
        return self.driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()



Browser = BrowserEngine()
driver = Browser.open_browser()
