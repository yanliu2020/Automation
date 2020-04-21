# -*- coding: utf-8 -*-

##导入工程绝对路径 jenkins执行本地文件
import os
import sys
run_path = os.path.abspath(__file__)
testrunner_path = os.path.dirname(run_path)
project_path = os.path.dirname(testrunner_path)
sys.path.append(project_path)
##

import unittest
from utils import HTMLTestRunner
from utils.datetime_helper import to_number
from utils.mail_helper import send_mail
from utils.basepath_helper import testsuites_path,report_path
FileName = to_number()

#待执行用例的目录
def runtest():
    testcase=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(testsuites_path,
                                                 pattern='test*.py',
                                                 top_level_dir=None)
    #discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            #添加用例到testcase
            testcase.addTest(test_case)
    # return testcase

    file_home= report_path + FileName + '_report.html'
    fp=open(file_home,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                         title="Automation Test Report",
                                         description="TestCase Execution:")

    runner.run(testcase)


if __name__=="__main__":
    runtest()
    from utils.browser_engine import Browser
    Browser.quit_browser()


    send_mail(report_path + FileName + '_report.html')  # 发送测试报告