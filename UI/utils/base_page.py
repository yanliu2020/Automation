#-*- coding: UTF-8 -*-
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from utils.basepath_helper import screenshots_path
from utils.logger import logger
#import win32gui
#import win32con
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    # 保存图片
    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\screenshots下
        """
        foldername = time.strftime('%Y%m%d', time.localtime(time.time()))  # 获取当前日期，创建一个当前日期的文件夹
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # file_path = os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + "..") + '/screenshots/' + foldername
        file_path = screenshots_path + foldername
        if not os.path.exists(file_path):            # 判断目录是否存在，不存在创建
            os.makedirs(file_path)
        screen_name = file_path + '/' + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

    def insert_img(self, file_name):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        base_dir = str(base_dir)
        base_dir = base_dir.replace('\\', '/')
        base = base_dir.split('test_case')[0]
        file_path = base + "report/image/" + file_name
        self.driver.get_screenshot_as_file(file_path)

    def find_element_by_wait(self, selector_by, selector_value):
        # element = None
        self.sleep(1.5)
        try:
            # element = self.driver.find_element_by_id(selector_value)
            element = WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located((selector_by, selector_value))
            )
            logger.info("Had find the element \' %s \' successful "
                        "by %s via value: %s " % (element.text, selector_by, selector_value))
        except TimeoutException:
            logger.error("TimeoutException: selector by %s ,value %s" % (selector_by, selector_value))
        except StaleElementReferenceException:
            logger.warning(msg='StaleElementReferenceException: %s , %s' % (selector_by, selector_value))
            return self.find_element_by_wait(selector_by, selector_value)
        else:
            return element

    def find_element(self, selector):
        """
         这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: element
        """
        element = None
        if '=>' not in selector:
            element = self.find_element_by_wait(By.ID, selector)
            if element is None:
                raise NoSuchElementException(msg='NoSuchElement: selector by.id value %s' % selector)
            else:
                return element
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        # 通过8中方式对元素进行定位
        if selector_by == "i" or selector_by == 'id':
            element = self.find_element_by_wait(By.ID, selector_value)

        elif selector_by == "n" or selector_by == 'name':
            element = self.find_element_by_wait(By.NAME, selector_value)

        elif selector_by == "c" or selector_by == 'class_name':
            element = self.find_element_by_wait(By.CLASS_NAME, selector_value)

        elif selector_by == "l" or selector_by == 'link_text':
            element = self.find_element_by_wait(By.LINK_TEXT, selector_value)

        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.find_element_by_wait(By.PARTIAL_LINK_TEXT, selector_value)

        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.find_element_by_wait(By.TAG_NAME, selector_value)

        elif selector_by == "x" or selector_by == 'xpath':
            element = self.find_element_by_wait(By.XPATH, selector_value)

        elif selector_by == "css" or selector_by == 'css_selector':
            element = self.find_element_by_wait(By.CSS_SELECTOR, selector_value)

        else:
            raise NameError("Please enter a valid type of targeting elements.")
        if element is None:
            logger.error('NoSuchElement selector_by: %s, selector: %s ' % (selector_by, selector_value))
            raise NoSuchElementException(msg="NoSuchElement:selector by %s ,value %s" % (selector_by, selector_value))
        else:
            return element

    # 输入
    def type(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

    # 清除文本框
    def clear(self, selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    # 点击元素
    def click(self, selector):

        el = self.find_element(selector)
        try:
            text = el.text
            el.click()
            logger.info("The element \' %s \' was clicked." % text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    # 显示等待时间
    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        # logger.info("Sleep for %d seconds" % seconds)

    # 返回当前页面网址
    def on_page(self):
        self.sleep(1)
        return self.driver.current_url

    # def find_element(self, *selector):
    #     return self.driver.find_element(*selector)

    # 火狐浏览器上传窗口配置
   # def file_import(self, filename):
    #    logger.info("The start configuring the firefox browser upload window")
    #   dialog = win32gui.FindWindow('#32770', u'文件上传')  # 对话框
    #    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    #    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    #    # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
    #    Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
    #    button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
    #    win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, filename)  # 往输入框输入绝对地址
    #    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
    #    logger.info("The file is uploaded successfully, the file name is %s" % filename)

    # 进入iframe框架
    def input_iframe(self, selector):
        el = self.find_element(selector)
        try:
            self.driver.switch_to.frame(el)
            logger.info("The iframe was clicked")
        except NameError as e:
            logger.error("Failed to click the iframe with %s" % e)

    # 返回上一级框架
    def back_iframe(self):
        try:
            self.driver.switch_to.default_content()
            logger.info("The iframe was quit")
        except NameError as e:
            logger.error("Failed to quit the iframe with %s" % e)

    # 移动元素
    def move_to_element(self, selector):
        try:
            logger.info("start move to element ")
            return ActionChains(self.driver).move_to_element(self.find_element(selector)).perform()
        except Exception as e:
            logger.error("Failed to move to element with %s" % e)
            return format(e)

    def find_elements_by_wait(self, selector_by, selector_value):
        # element = None
        self.sleep(0.5)
        try:
            # element = self.driver.find_element_by_id(selector_value)
            element = WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_all_elements_located((selector_by, selector_value))
            )
            logger.info("Had find the elements successful "
                        "by %s via value: %s " % (selector_by, selector_value))
        except TimeoutException:
            logger.error("TimeoutException: selector by %s ,value %s" % (selector_by, selector_value))
        except StaleElementReferenceException:
            logger.warning(msg='StaleElementReferenceException: %s , %s' % (selector_by, selector_value))
            return self.find_elements_by_wait(selector_by, selector_value)
        else:
            return element

    def find_elements(self, selector):
        """
         这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: element
        """
        elements = []
        if '=>' not in selector:
            elements = self.find_elements_by_wait(By.ID, selector)
            if len(elements) < 1:
                raise NoSuchElementException(msg='NoSuchElement: selector by.id value %s' % selector)
            else:
                return elements
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        # 通过8中方式对元素进行定位
        if selector_by == "i" or selector_by == 'id':
            elements = self.find_elements_by_wait(By.ID, selector_value)

        elif selector_by == "n" or selector_by == 'name':
            elements = self.find_elements_by_wait(By.NAME, selector_value)

        elif selector_by == "c" or selector_by == 'class_name':
            elements = self.find_elements_by_wait(By.CLASS_NAME, selector_value)

        elif selector_by == "l" or selector_by == 'link_text':
            elements = self.find_elements_by_wait(By.LINK_TEXT, selector_value)

        elif selector_by == "p" or selector_by == 'partial_link_text':
            elements = self.find_elements_by_wait(By.PARTIAL_LINK_TEXT, selector_value)

        elif selector_by == "t" or selector_by == 'tag_name':
            elements = self.find_elements_by_wait(By.TAG_NAME, selector_value)

        elif selector_by == "x" or selector_by == 'xpath':
            elements = self.find_elements_by_wait(By.XPATH, selector_value)

        elif selector_by == "css" or selector_by == 'css_selector':
            elements = self.find_elements_by_wait(By.CSS_SELECTOR, selector_value)

        else:
            raise NameError("Please enter a valid type of targeting elements.")
        if elements is None:
            raise NoSuchElementException(msg="NoSuchElements:selector by %s ,value %s" % (selector_by, selector_value))
        else:
            return elements

    def is_active(self, selector):
        """
        # 检查元素是否为选中状态
        :param selector:
        :return:
        """
        element = self.find_element(selector)
        class_attr = element.get_attribute('class')
        if 'active' in class_attr:
            return True
        else:
            return False

    def scroll_into_view(self,selector):
        """
        # 滚动页面，至元素位置
        # 适用于页面未分页，元素未出现在页面可视范围内时
        :param selector:
        :return:
        """
        # self.driver.execute_script("arguments[0].scrollIntoView(false);", element)
        element = self.find_element(selector)
        element.location_once_scrolled_into_view

    def get_page_title(self):
        """
        # 获取页面标题
        :return:
        """
        return self.driver.title

    def refresh_page(self):
        """
        # 刷新当前页面
        :return:
        """
        self.driver.refresh()

    def mouse_into_element(self, element):
        """
        # 焦点移动到元素
        :param element:
        :return:
        """
        location = element.location
        # x = -100
        y = -200
        # if location['x'] < 300:
        #     x = 100
        if location['y'] < 400:
            y = 200
        ActionChains(self.driver).move_to_element_with_offset(element, 0, y).perform()
        ActionChains(self.driver).move_to_element(element).perform()

    def swith_to_handle(self,flag):
        """
        # 新窗口打开,切换至新窗口操作
        :param window,flag:
        :return:
        """
        window = self.driver.current_window_handle()
        windows = self.driver.window_handles()
        for current_window in windows:
            if current_window != window and flag == 1:
                self.driver.switch_to.window(current_window)
            elif flag == 0:
                self.driver.switch_to.window(windows[0])

    def drag_and_drop(self,source_selector,target_selector):
        """拖拽
        :param source_selector,target_selector:
        :return:
        """
        source = self.find_element(source_selector)
        target = self.find_element(target_selector)
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    def drop_select(self,selector,value):
        """下拉框选择
        :param selector
        :param value: option value=
        :return:
        """
        self.click(selector)
        Select(self.find_element(selector)).select_by_value(value)

    def ctrl_all(self,selector):
        """全选操作
        :param selector
        :return:
        """
        self.click(selector)
        self.find_element(selector).send_keys(Keys.CONTROL,'a')
        self.find_element(selector).send_keys(Keys.BACKSPACE)

