-- 排序

    -- order by 字段
    -- asc(默认) 从小到大排序，即升序
    -- desc 从大到小排，即降序

    -- 查询18-60的女性，按照年龄从小到大排序
    select * from student where (age between 18 and 60) and gender="女" order by age;

    -- 查询18-60的女性，按照年龄从大到小排序,如果年龄相同，则按照id从大到小排
    select * from student where (age between 18 and 60) and gender="女" order by age desc,id desc;