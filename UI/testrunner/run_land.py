# -*- coding: utf-8 -*-

##导入工程绝对路径 jenkins执行本地文件
import os
import sys
run_path = os.path.abspath(__file__)
testrunner_path = os.path.dirname(run_path)
project_path = os.path.dirname(testrunner_path)
sys.path.append(project_path)
##

import  unittest
from utils import  HTMLTestRunner_cn
from utils.mail_helper import send_mail
from utils.datetime_helper import  to_number
from utils.basepath_helper import  testsuites_path,report_path


file_name = to_number()

def runtest():
    discover01 = unittest.TestLoader().discover(
        start_dir=testsuites_path + "test_land_module//", pattern='test_01_*.py', top_level_dir=None)
    discover02 = unittest.TestLoader().discover(
        start_dir=testsuites_path + "test_land_module//", pattern='test_08_*.py', top_level_dir=None)
    discover03 = unittest.TestLoader().discover(
        start_dir=testsuites_path + "test_land_module//", pattern='test_09_*.py', top_level_dir=None)

    testsuite = unittest.TestSuite()
    testsuite.addTest(discover01)
    testsuite.addTest(discover02)
    testsuite.addTest(discover03)

    filename = report_path + file_name + '_report.html'

    with open(filename,'wb') as fp:
        runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title='UI Automation for Land',description='Testcase Excution:')
        runner.run(testsuite)


def testrun():
    runtest()
    from utils.browser_engine import Browser
    Browser.quit_browser()
    send_mail(report_path + file_name + '_report.html')  # 发送测试报告


if __name__== '__main__':
    testrun()



