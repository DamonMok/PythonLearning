-- 范围查询

    -- 1 查询非连续的范围
    -- 1.1 in
    -- 查询年龄为8、18、30的学生
    select * from student where age in (8,18,30);

    -- 1.2 not in
    -- 查询年龄不是8、18、30的学生
    select * from student where age not in (8,18,30);




    -- 2 查询连续的范围
    -- 2.1 between and
    -- 查询年龄为18~30的学生
    select * from student where age between 18 and 30;

    -- 2.2 not between and
    -- 查询年龄非18~30的学生
    select * from student where age not between 18 and 30;
    -- 失败，not between是一个整体，不可以拆
    -- select * from student where age not (between 18 and 30);




    -- 3 空判断
    -- 3.1 is null
    -- 判断生日为空的学生
    select * from student where birth is null;

    -- 3.2 is not null
    --判断生日为空的学生
    select * from student where birth is not null;


