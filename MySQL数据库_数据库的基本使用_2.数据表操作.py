-- 数据表的操作

    -- 创建表(student表)
    -- auto_increment 表示自动增长
    -- not null 不能为空
    -- primary key 主键
    -- default 默认值
    -- 格式：create table 数据表名字 (字段 类型 约束)
    create table student (
        id int unsigned not null auto_increment primary key, -- unsigned无符号，只有正数
        name varchar(30),
        age tinyint unsigned default 0,
        high decimal(5,2),  -- 五位数，其中小数占2位
        gender enum("男","女","保密") default "保密",  -- 枚举
        cls_id int unsigned
    );



    -- 查看表结构
    desc student

    +--------+----------------------------+------+-----+---------+----------------+
    | Field  | Type                       | Null | Key | Default | Extra          |
    +--------+----------------------------+------+-----+---------+----------------+
    | id     | int unsigned               | NO   | PRI | NULL    | auto_increment |
    | name   | varchar(30)                | YES  |     | NULL    |                |
    | age    | tinyint unsigned           | YES  |     | 0       |                |
    | high   | decimal(5,2)               | YES  |     | NULL    |                |
    | gender | enum('男','女','保密')       | YES  |     | 保密     |                |
    | cls_id | int unsigned               | YES  |     | NULL    |                |
    +--------+----------------------------+------+-----+---------+----------------+



    -- 查看表的创建语句
    show create table student;

    | student | CREATE TABLE `student` (
      `id` int unsigned NOT NULL AUTO_INCREMENT,
      `name` varchar(30) DEFAULT NULL,
      `age` tinyint unsigned DEFAULT '0',
      `high` decimal(5,2) DEFAULT NULL,
      `gender` enum('男','女','保密') DEFAULT '保密',
      `cls_id` int unsigned DEFAULT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci



    -- 修改表-添加字段
    alter table student add birthday datetime;



    -- 修改表-修改字段约束
    alter table student modify birthday date;



    -- 修改表-修改字段名字和约束
    alter table student change birthday birth datetime default "1990-12-16";



    -- 修改表-删除字段
    alter table student drop high;

