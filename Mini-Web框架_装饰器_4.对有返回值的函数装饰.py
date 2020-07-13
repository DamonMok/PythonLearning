def set_func(func):

    def call_func(*args, **kwargs):
        print("权限验证1")
        print("权限验证2")
        return func(*args, **kwargs)
    return call_func


# test1等于call_func,当执行到func(*args, **kwargs)时，
@set_func
def test1(num, *args, **kwargs):
    print("-----test1-----%d", num)
    print("-----test1-----%d", args)
    print("-----test1-----%d", kwargs)
    return "ok"


ret = test1(100)
print(ret)

