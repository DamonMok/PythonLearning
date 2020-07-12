-- 条件查询


    -- 1.比较运算符(> / < / >= / <= / = / !=)
    -- 查询年龄大于18的数据
    select * from student where age>18;




    -- 2.逻辑运算符(and/or/not)
    -- 查询年龄18~35之间的数据
    select * from student where age>18 and age<35;





    -- 3.模糊查询
    -- 3.1 like(%替换多个,_替换一个)
    -- 查询以"张"开头的学生
    select * from student where name like "张%";

    -- 查询名字有两个字的学生
    select * from student where name like "__";

    -- 查询名字至少有两个字的学生
    select * from student where name like "__%";


    —— 3.2 rlike(正则)
    -- 查询以"张"开头的学生
    select * from student where name rlike "^张.*";

    -- 查询以"张"开头并且以"猪"结尾的学生
    select * from student where name rlike "^张.*猪$";




