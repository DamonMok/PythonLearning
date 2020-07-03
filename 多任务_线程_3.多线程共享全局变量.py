import time
import threading

glb_num = 100


def test1():
    global glb_num
    glb_num += 1
    print(glb_num)


def test2():
    print(glb_num)


def main():

    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    
    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print(glb_num)


if __name__ == '__main__':
    main()
