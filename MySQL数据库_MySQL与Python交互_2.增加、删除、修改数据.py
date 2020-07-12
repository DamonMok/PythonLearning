from pymysql import *


def main():
    # 1.创建数据库连接
    conn = connect(host="localhost", port=3306, user="root", password="damonmok", database="python_db")

    # 2.获取游标对象
    cursor = conn.cursor()

    # 3.1 新增数据并返回受影响的函数
    # count = cursor.execute('insert into student values (default,"张小猪", 22, "保密", 3, "1998-01-01", 0)')

    # 3.2 修改数据并返回受影响的函数
    # count = cursor.execute('update student set name="张大猪" where id=3')

    # 3.3 删除数据并返回受影响的函数
    # count = cursor.execute('delete from student where id=4')
    # print(count)

    # 4 执行查询，并返回受影响的函数
    count = cursor.execute('select * from student')
    print("查询到%d条数据" % count)

    # 5.获取查询到的数据
    # 5.1 cursor.fetchone() 一条一条地取结果
    # for i in range(count):
    #     rst = cursor.fetchone()
    #     print(rst)

    # 5.2 fetchmany()  # 默认一条条取，有指定参数就按照参数的数量取
    # rst = cursor.fetchmany(3)
    # print(rst)

    # 5.3 fetchall()  # 全部取出
    rst = cursor.fetchall()
    print(rst)

    # 6.关闭游标对象、关闭数据库连接
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
