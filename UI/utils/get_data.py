# coding:utf-8
import xlrd

# filepath = "E:\\Automation\\UI\\testdata\\testdata.xlsx"
# sheetName = "new_customer"
class excelHandle(object):
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # # 获取第一行作为key值
        # self.keys = self.table.row_values(0)
        # # 获取总行数
        # self.rowNum = self.table.nrows
        # # 获取总列数
        # self.colNum = self.table.ncols

    def read_excel(self):
        rows = []
        for row_idx in range(1, self.table.nrows):  # iterate 1 to maxrows
            rows.append(list(self.table.row_values(row_idx, 0, self.table.ncols)))
        return rows


if __name__ == "__main__":
    filepath = "E:\\Automation\\UI\\getdata\\testData.xlsx"
    sheetName = "new_customer"
    data = excelHandle(filepath, sheetName).read_excel()
    print(data)
    print(type(data))
