# -*- coding:utf-8 -*-

import os

#当前文件路径
abs_path = os.path.abspath(__file__)

# 当前文件上一层目录名
utils_path = os.path.dirname(abs_path)

# \test_fz_auto\fangzhou 工程目录
project_path = os.path.dirname(utils_path)

# \test_fz_auto\fangzhou\utils\conf\
conf_path = utils_path + os.path.sep + 'conf' + os.path.sep

# \test_fz_auto\fangzhou\ 工程目录
base_path = os.path.dirname(utils_path) + os.path.sep

# \test_fz_auto\fangzhou\screenshots\
screenshots_path = base_path + 'screenshots' + os.path.sep

if not os.path.exists(screenshots_path):
    os.makedirs(screenshots_path)

# \test_fz_auto\fangzhou\report\
report_path = base_path + 'report' + os.path.sep

if not os.path.exists(report_path):
    os.makedirs(report_path)

# \test_fz_auto\fangzhou\drivers\
drivers_path = base_path + 'drivers' + os.path.sep

# \test_fz_auto\fangzhou\logs\
logs_path = base_path + 'logs' + os.path.sep

if not os.path.exists(logs_path):
    os.makedirs(logs_path)

# \test_fz_auto\fangzhou\testsuites\
testsuites_path = base_path + 'testsuites' + os.path.sep

# \test_fz_auto\fangzhou\config\
config_path = base_path + 'config' + os.path.sep

# \test_fz_auto
sys_path = os.path.dirname(project_path)

#test_fz_auto\UI\utils
utils_path = base_path + 'utils' + os.path.sep

#UI\getData
excel_path= base_path + 'getdata' + os.path.sep

