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
import threading
from utils import  HTMLTestRunner
from utils.mail_helper import send_mail
from utils.datetime_helper import  to_number
from utils.basepath_helper import  testsuites_path,report_path
file_name = to_number()

def allcase():
    discover = unittest.defaultTestLoader.discover(testsuites_path, pattern='test_*.py', top_level_dir=None)
    # testsuite = unittest.TestSuite()
    # for test_suite in discover:
    #     for test_case in test_suite:
    #         testsuite.addTest(test_case)
    # testsuite = unittest.TestSuite()
    # testsuite.addTest(discover)
    return discover


def runcase(suite):
    filename = report_path + file_name + '_report.html'
    fp = open(filename, "wb")
    proclist = []
    s = 0
    for i in suite:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='UI Automation Test Report',
                                               description='Testcase Excution:')
    proc = threading.Thread(target=runner.run, args=(i,))
    proclist.append(proc)
    s = s + 1
    for proc in proclist:
         proc.start()

    for proc in proclist:
        proc.join()

    fp.close()
    send_mail(report_path + file_name + '_report.html')  # 发送测试报告


if __name__== '__main__':
    runtmp = allcase()
    runcase(runtmp)



