# -*- coding:utf-8 -*-
import time
from configparser import ConfigParser
from selenium import webdriver
from pageobjects.login.login import SystemLogin
from config.login.login_entity import  LoginEntity
from utils.basepath_helper import logs_path, project_path, drivers_path, config_path,utils_path,download_path
from utils.logger import logger
from utils.base_page import BasePage

class BrowserEngine(object):
    chrome_driver_path = drivers_path + 'chromedriver.exe'
    firefox_driver_path = drivers_path + 'geckodriver.exe'
    ie_driver_path = drivers_path + 'IEDriverServer.exe'
    edge_driver_path = 'C:\\Windows\\SysWOW64\\MicrosoftWebDriver.exe'
    geckodriver_path = utils_path + 'geckodriver.log'
    dir_name = time.strftime("%Y-%m-%d", time.localtime())
    download_file_path = download_path + dir_name

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
            profile.set_preference('browser.download.dir', self.download_file_path)
            profile.set_preference('browser.download.folderList', 2)
            profile.set_preference('browser.download.manager.showWhenStarting', False)
            profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/octet-stream, application/vnd.ms-excel, text/csv, application/zip')
            self.driver = webdriver.Firefox(firefox_profile=profile, executable_path=self.firefox_driver_path,
                                            log_path=self.geckodriver_path)
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            options = webdriver.ChromeOptions()
            prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': self.download_file_path}
            options.add_experimental_option('prefs', prefs)
            self.driver = webdriver.Chrome(self.chrome_driver_path,chrome_options=options)
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            self.driver = webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser.")
        elif browser == "Edge":
            self.driver = webdriver.Edge(self.edge_driver_path)
            logger.info("Starting Edge browser.")

        self.driver.maximize_window()
        """
        # ?????????????????????????????????1024*768????????????????????????????????????
        # ???????????????????????????????????????????????????????????????????????????????????????
        """
        #self.driver.set_window_size(1920, 1080)
        logger.info("Maximize the current window.")

        self.driver.get(url)
        logger.info("Open url: %s" % url)

        # self.driver.implicitly_wait(3)
        # logger.info("Set implicitly wait 10 seconds.")

        BasePage(self.driver).find_element_by_wait('xpath',LoginEntity.login_title)

        #input login account
        SystemLogin(self.driver).user_login('yan.liu@an-chen.com','Lychan@2012')
        return self.driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()



Browser = BrowserEngine()
driver = Browser.open_browser()
