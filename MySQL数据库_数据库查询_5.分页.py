-- 分页

    -- limit * start,count
    -- 限制查询出来的数据个数
    select * from student limit 2;

    -- 查询前3个数据
    select * from student limit 0,3;

    -- 每页显示2个，查询第1页
    select * from student limit 0,2;

    -- 每页显示2个，查询第2页
    select * from student limit 2,2;

    -- 每页显示2个，查询第3页
    select * from student limit 4,2;

    -- 每页显示2个，查询第n页
    -- 失败(不能写表达式) select * from student limit (n-1)*2,2;
    -- 失败(limit要写最后面) select * from student limit 5 order by gender desc;