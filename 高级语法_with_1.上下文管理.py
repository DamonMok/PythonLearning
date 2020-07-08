class File(object):
    def __init__(self, file_name, mode):

        self.file_name = file_name
        self.mode = mode

    # 开始时会调用这个方法
    def __enter__(self):
        print("entering")
        self.f = open(self.file_name, self.mode)
        return self.f  # 返回调用with时需要用来处理事情的对象(as后面的对象)

    # 结束前会调用这个方法
    def __exit__(self, *args):
        print("will exit")
        self.f.close()


with File("test.txt", "w") as f:
    # 中间处理事情
    print("writing")
    f.write("hello, python!")
