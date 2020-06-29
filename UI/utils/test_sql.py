import pymssql #引入pymssql模块


def conn():
    connect = pymssql.connect('rralamosqltest.southcentralus.cloudapp.azure.com', 'yan.liu', 'Lychan@202005', 'MCDH')
    if connect:
        print("连接成功!")
        
    return connect


if __name__ == '__main__':
    conn = conn()