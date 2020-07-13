def set_func1(func):

    print("开始用set_func1装饰")
    def call_func(*args, **kwargs):
        print("set_func1权限验证1")
        print("set_func1权限验证2")
        return func(*args, **kwargs)
    return call_func

def set_func2(func):

    print("开始用set_func2装饰")
    def call_func(*args, **kwargs):
        print("set_func2权限验证1")
        print("set_func2权限验证2")
        return func(*args, **kwargs)
    return call_func


# 外层：先1后2
# 里层：先2后1
@set_func2
@set_func1
def test1(num, *args, **kwargs):
    return "ok"


ret = test1(100)
print(ret)

