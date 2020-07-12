-- 数据的增删改查(curd)

    +--------+----------------------------+------+-----+---------+----------------+
    | Field  | Type                       | Null | Key | Default | Extra          |
    +--------+----------------------------+------+-----+---------+----------------+
    | id     | int unsigned               | NO   | PRI | NULL    | auto_increment |
    | name   | varchar(30)                | YES  |     | NULL    |                |
    | age    | tinyint unsigned           | YES  |     | 0       |                |
    | gender | enum('男','女','保密')     | YES  |     | 保密    |                |
    | cls_id | int unsigned               | YES  |     | NULL    |                |
    | birth  | date                       | YES  |     | NULL    |                |
    +--------+----------------------------+------+-----+---------+----------------+

    -- 增加-全列插入
    -- 1.自增主键可以用0,null,default代替
    -- 2.枚举从1开始，可以用【值】或者【数字】代替
    insert into student values (0,"damon",20,"男",6,"1990-12-16");
    insert into student values (null,"damon",20,1,6,"1990-12-16");
    insert into student values (default,"damon",20,2,6,"1990-12-16");

    -- 增加-部分插入
    insert into student (name,gender) values ("张猪猪","女");





    -- 修改-全部修改
    update student set age=20;

    -- 修改-部分修改
    update student set gender="女" where name="张猪猪";
    update student set age=18, birth="1996-06-08" where name="张猪猪";





    -- 查询-全部查询
    select * from student;

    -- 查询-指定条件查询
    select * from student where name="张猪猪";
    select * from student where id>2;

    -- 查询-查询指定列
    select name,gender from student;

    -- 查询-查询指定列,并且给列起名
    select name as 姓名,gender as 性别 from student;
    select student.name,student.age from student
    select s.name,s.age from student as s

    -- 查询-消除重复行
    select distinct from students;




    -- 物理删除-全部删除
    delete from student;

    -- 物理删除-删除指定的数据
    delete from student where name="damon";

    -- 逻辑删除(新增一个删除标识字段，用以表示是否已经删除)
    alter table student add is_delete bit default 0;
    update student set is_delete=1 where id=4;

