import time
import threading


def sing():
    for i in range(5):
        print("sing:%s" % i)
        time.sleep(1)


def dance():
    for i in range(5):
        print("dance:%s" % i)
        time.sleep(1)


def main():
    """多线程唱歌跳舞"""

    # 1.创建多线程
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    # 2.开启多线程
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
