class Test(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("权限验证")
        return self.func()


@Test  # 等于：get_str = Test(get_str)
def get_str(*args, **kwargs):
    return "ok"


# 实例对象get_str调用()，等于调用__call__方法
print(get_str())

