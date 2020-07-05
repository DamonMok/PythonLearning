import time
from greenlet import greenlet


def task1():
    while True:
        print("-"*20)
        print("---task1---")
        grl2.switch()
        time.sleep(0.1)


def task2():
    while True:
        print("---task2---")
        grl1.switch()
        time.sleep(0.1)


grl1 = greenlet(task1)
grl2 = greenlet(task2)


def main():

    """使用greenlet完成多任务"""
    # 需要首先 sudo pip3 install greenlet

    grl1.switch()


if __name__ == '__main__':
    main()


