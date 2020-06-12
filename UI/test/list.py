# coding=utf-8
import xlrd
import sys


import traceback
from datetime import datetime
from xlrd import xldate_as_tuple


class excelHandle(object):

    def read_excel(self, filename, sheetname):
        rbook = xlrd.open_workbook(filename)
        sheet = rbook.sheet_by_name(sheetname)
        rows = sheet.nrows
        cols = sheet.ncols
        all_content = []
        j = 1
        for i in range(rows):
            row_content = []
            if i != 0:
                for j in range(cols):
                    ctype = sheet.cell(i, j).ctype  # 表格的数据类型
                    cell = sheet.cell_value(i, j)
                    if ctype == 2 and cell % 1 == 0:  # 如果是整形
                        cell = int(cell)
                    elif ctype == 3:
                        # 转成datetime对象
                        date = datetime(*xldate_as_tuple(cell, 0))
                        cell = date.strftime('%Y/%d/%m %H:%M:%S')
                    elif ctype == 4:
                        cell = True if cell == 1 else False
                    row_content.append(cell)
                    j += 1
                all_content.append(row_content)
            # print('[' + ','.join("'" + str(element) + "'" for element in row_content) + ']')
        print(all_content)
        print(all_content[0][:])
        return all_content




# if __name__ == '__main__':
#     eh = excelHandle()
#     filename = "E:\\Automation\\UI\\test\\test.xlsx"
#     sheetname = "new_customer"
#     eh.read_excel(filename, sheetname)
