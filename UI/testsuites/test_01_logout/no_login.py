from selenium import webdriver
from testsuites.test_01_logout.myFirefox import  ReuseChrome
from utils.basepath_helper import drivers_path
from utils.browser_engine import driver

#  第一次使用Chrome() 新建浏览器会话
chrome_driver_path = drivers_path + 'chromedriver.exe'
driver = driver


# 记录 executor_url 和 session_id 以便复用session
executor_url = driver.command_executor._url
session_id = driver.session_id
# 访问百度
driver.get("https://rralamotest.z21.web.core.windows.net/")

print(session_id)
print(executor_url)

# 假如driver对象不存在，但浏览器未关闭
del driver

# 使用ReuseChrome()复用上次的session
driver2 = ReuseChrome(command_executor=executor_url, session_id=session_id)

# 打印current_url为百度的地址，说明复用成功
print(driver2.current_url)
driver2.get("https://rralamotest.z21.web.core.windows.net/")
