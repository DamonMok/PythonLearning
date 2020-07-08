from contextlib import contextmanager


@contextmanager
def my_file(path, mode):
    f = open(path, mode)  # 之前做的事
    yield f  # 返回调用时需要用到的对象
    f.close()  # 之后做的事


with my_file("test.txt", "w") as f1:
    f1.write("hello, python!")  # 中间做的事
