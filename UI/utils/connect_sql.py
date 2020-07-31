#!coding:utf-8
import pymssql
import  random

class dbConnect(object):
    def getdata(self,dbName,fieldName,param):
        connect = pymssql.connect('rralamosqltest.southcentralus.cloudapp.azure.com', 'yan.liu', 'Lychan@202007',
                                  dbName)
        # connect = pymssql.connect('rralamosqldev.southcentralus.cloudapp.azure.com', 'Chris.Guo', 'Alamo617*',
        #                           dbName)
        cur = connect.cursor()
        # sql = "SELECT varAddressType FROM ltblAddressType"
        # sqlvalue = sql  # "select * from user"
        try:
            if fieldName == "salutation":
                sqlvalue = "SELECT varSalutation FROM ltblSalutation"
            elif fieldName == "suffix":
                sqlvalue = "SELECT varSuffix FROM ltblSuffix"
            elif fieldName == "stateOfIncorporation" or fieldName == "stateCode":
                sqlvalue = "SELECT varState FROM vewLookupState"
            elif fieldName == "emailType":
                sqlvalue = "SELECT varEmailType FROM ltblEmailType"
            elif fieldName == "phoneType":
                sqlvalue = "SELECT varPhoneType FROM ltblPhoneType"
            elif fieldName == "roleType":
                sqlvalue = "select top(10) varContactRole FROM ltblContactRole order by intContactRoleSystemId asc"
            elif fieldName == "addressType":
                sqlvalue = "SELECT varAddressType FROM ltblAddressType"
            elif fieldName == "identifierName":
                sqlvalue = "SELECT varIdentifierName FROM ltblIdentifierName "
            elif fieldName == "identifierNameWithoutBan":
                sqlvalue = "SELECT varIdentifierName FROM vewLookupIdentifierNameWithoutBan"
            elif fieldName == "CustomerId_Organization":
                sqlvalue = "SELECT varBusinessEntityId from tblBusinessEntity where varOrganizationName = '%s' and datInactiveDate is NULL" %(param)
            elif fieldName == "CustomerId_Person":
                sqlvalue = "SELECT varBusinessEntityId from tblBusinessEntity where varFullName = '%s' and datInactiveDate is NULL" %(param)
            cur.execute(sqlvalue)
            results = cur.fetchall()
            testData = random.choice(results)[0]
            # print(testData)
            return  testData

        except:
            print('Error:unable to fetch data')
        # self.connect.close()

# if __name__ == '__main__':
#     res = dbConnect().getdata('MCDH','CustomerId_Person','Miss I4JyD5 QNWCnb OfT3Jz Sr.')
    # data = random.choice(res)[0]
#     # print(data)
