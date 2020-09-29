#!coding:utf-8
import pymssql
import functools
import  random

class dbConnect(object):
    def getdata(self,fielName,dbName,table,varField):
        connect = pymssql.connect('rralamosqltest.southcentralus.cloudapp.azure.com', 'yan.liu', 'Lychan@202008',
                                  dbName)
        # connect = pymssql.connect('rralamosqldev.southcentralus.cloudapp.azure.com', 'Chris.Guo', 'Alamo617*',
        #                           dbName)
        cur = connect.cursor()
        # sql = "SELECT varAddressType FROM ltblAddressType"
        # sqlvalue = sql  # "select * from user"
        try:
            if fielName != "":
                sqlvalue = "SELECT %s FROM %s" % (varField, table)
                cur.execute(sqlvalue)
                results = cur.fetchall()
                # 拆开一层嵌套列表元组
                rows = functools.reduce(lambda x, y: x + y, results)
                testData = rows[random.randint(0, len(rows) - 1)]
                # print("#######")
                # print(testData)
                # print("#######")
                return testData
        except:
            print('Error:unable to fetch data')
        # self.connect.close()

# if __name__ == '__main__':
#     res = dbConnect().getdata('ALAMO','ltblInterestClass','varInterestClass')

