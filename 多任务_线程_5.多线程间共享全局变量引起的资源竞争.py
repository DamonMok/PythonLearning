import threading


glb_num = 100


def test1(loop_times):
    # glb_num += 1  运行时，转化为：glb_num = glb_num + 1
    # 在test1的glb_num + 1时，如果还没赋值，就被test2把glob_num的值修改了
    # 就会发生数据混乱
    for i in range(loop_times):
        global glb_num
        glb_num += 1

    print(glb_num)


def test2(loop_times):

    for i in range(loop_times):
        global glb_num
        glb_num += 1

    print(glb_num)


def main():

    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("main thread -- glb = %d" % glb_num)


if __name__ == '__main__':
    main()
