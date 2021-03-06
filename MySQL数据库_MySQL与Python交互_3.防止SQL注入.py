from pymysql import *


def main():
    # 1.创建数据库连接
    conn = connect(host="localhost", port=3306, user="root", password="damonmok", database="python_db")

    # 2.获取游标对象
    cursor = conn.cursor()

    # 3.执行查询，并返回受影响的函数
    # 这里把要查询的关键字，以参数(params)的形式传给execute,让mysql去作防注入处理
    search_name = "张猪猪"
    params = [search_name]
    count = cursor.execute('select * from student where name=%s', params)
    print("查询到%d条数据" % count)

    # 4.获取查询到的数据
    # 4.1 cursor.fetchone() 一条一条地取结果
    # for i in range(count):
    #     rst = cursor.fetchone()
    #     print(rst)

    # 4.2 fetchmany()  # 默认一条条取，有指定参数就按照参数的数量取
    # rst = cursor.fetchmany(3)
    # print(rst)

    # 4.3 fetchall()  # 全部取出
    rst = cursor.fetchall()
    print(rst)

    # 5.关闭游标对象、关闭数据库连接
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
