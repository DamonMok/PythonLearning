def set_func1(func):
    def call_func1():
        print("权限验证1")
        print("权限验证2")
        func()
    return call_func1


# 1.对无参数函数装饰
@set_func1
def test1():
    print("-----test1-----")


def set_func2(func):
    def call_func2(num):
        print("权限验证1")
        print("权限验证2")
        func(num)
    return call_func2


# 2.对有参数函数装饰
@set_func2
def test2(num):
    print("-----test1-----%d" % num)


test1()
# test2等于set_func2的返回值->call_func;
# test2(100)相当于调用call_func2(100);
# call_func2里面的func指向test2，相当于调用test2(100)
test2(100)
