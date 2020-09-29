# coding:utf-8
import xlrd

# filepath = "E:\\Automation\\UI\\getdata\\TestData.xlsx"
# sheetName = "LandDictionaryList"
class excelHandle(object):
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        #获取第一列fieldName值
        self.param = self.table.col_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def read_excel(self,param):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1):
                s = {}
                # 从第二行取对应values值
                if self.table.cell_value(i,0) == param:
                    for x in range(self.colNum):
                        List=self.table.cell_value(i,x)
                        r.append(List)
                j += 1
            return r

# if __name__ == "__main__":
#     filepath = "E:\\Automation\\UI\\getdata\\TestData.xlsx"
#     sheetName = "LandDictionaryList"
#     data = excelHandle(filepath, sheetName).read_excel("Multi Tract Sale Indicator")
#     print(data)
#     print(type(data))
