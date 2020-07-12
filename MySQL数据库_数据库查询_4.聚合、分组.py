-- 聚合

    -- count(总数)
    -- 查询女性有多少人
    select count(*) as 女性 from student where gender="女";


    -- max(最大值)
    -- 查询女性中年龄最大值
    select max(age) from student where gender="女";


    -- min(最小值)
    -- 查询女性中年龄最小值
    select min(age) from student where gender="女";


    -- avg(平均值)
    -- 查询女性中年龄平均值
    select avg(age) from student where gender="女";


    -- round(四舍五入)
    -- 查询女性中年龄平均值,保留两位小数
    select round(avg(age),2) from student where gender="女";




-- 分组

    -- 1. group by分组
    -- 按照性别分组，查询所有的性别
    select gender from student group by gender;

    -- 按照性别分组，查询不同性别的人数
    select gender, count(*) from student group by gender;

    -- 按照性别分组，查询男性的人数
    select gender, count(*) from student where gender="男" group by gender;


    -- 2. group_concat()查看分组内的详情
    -- 按照性别分组，查询所有的性别的详细
    -- group_concat内有多个字段的话，需要隔开
    select gender,group_concat(name," ",age," ",birth) from student group by gender;


    -- 3. having(having是对分组后，每组的【聚合】结果进行过滤；where是对字段进行过滤)
    -- 查询平均年龄超过30岁的性别，以及姓名
    select gender,group_concat(name),avg(age) from student group by gender having avg(age)>20;

    -- 查询每种性别中，多于2人的信息
    select gender,group_concat(name),count(*) from student group by gender having count(*)>2;