-- 连接查询

    student(A,B,C)
    class(c1,c2,c3)

    -- 1. inner join ... on
    -- 查询所有能对应班级的学生以及班级信息
    select * from student inner join class on student.cls_id=class.id;

    -- 查询学生的姓名和对应的班级名字
    select student.name,class.name from student inner join class on student.cls_id=class.id;
    或者
    select s.name,c.name from student as s inner join class as c on s.cls_id=c.id;

    -- 查询学生的所有信息，以及班级名称
    select s.*,c.name from student as s inner join class as c on s.cls_id=c.id;


    -- 2. left join ...  on
    -- 查询每位学生对应的班级信息
    -- 以左边的student表为基准，【左边】学生信息全部显示，【右边】(班级id)对应得上(学生里面的班级id)的就显示，否则右边班级的数据显示为NULL
    select s.name,c.name from student as s left join class as c on s.cls_id=c.id;

    -- 查询没有对应班级信息的学生
    -- 把前面的查询结果，作为结果集，调用having来显示没有对应班级信息的学生数据
    select s.*,c.* from student as s left join class as c on s.cls_id=c.id having c.id is null;


    -- 3. right join ... on
    -- 和上面相反

