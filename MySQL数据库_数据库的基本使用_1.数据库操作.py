--数据库的操作

    -- 连接数据库(root是用户名、damonmok是密码)
    mysql -uroot -p
    或者
    mysql -uroot -pdamonmok

    -- 退出数据库
    exit/quit/ctrl+d

    -- 查看数据库版本
    select version();

    -- 查看时间
    select now();

    -- 查看所有数据库
    show databases;

    -- 查看当前使用的数据库
    select database();

    -- 使用数据库
    use python_db;

    -- 创建数据库(数据库名字为:python_db)
    create database python_db;  -- MySQL8.0之后默认编码为utf8mb4
    或
    create database python_db charset=utf8;  -- MySQL8.0之前默认编码为Latin拉丁

    -- 查看数据库创建的语句(查看数据库是怎么创建的)
    show create database python_db;

    +-----------+-------------------------------------------------------------------------------------------------------------------------------------+
    | Database  | Create Database                                                                                                                     |
    +-----------+-------------------------------------------------------------------------------------------------------------------------------------+
    | python_db | CREATE DATABASE `python_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */ |
    +-----------+-------------------------------------------------------------------------------------------------------------------------------------+

    -- 删除数据库
    drop database python_db;