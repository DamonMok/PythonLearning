import threading
import time


class MyThread(threading.Thread):

    """线程开启后，会自动调用该方法"""
    def run(self):
        for i in range(5):
            msg = "I'm " + self.name + ' @ ' + str(i)
            print(msg)
            time.sleep(1)


if __name__ == '__main__':

    # 1.通过继承 Thread类 创建线程
    t1 = MyThread()
    t2 = MyThread()

    # 2.开启线程
    t1.start()
    t2.start()
