
def main():
    # 生成器是一个特殊的迭代器

    # 是一个数组，浪费内存空间
    num1 = [i*2 for i in range(10)]  # 通过列表推导式生成

    print(num1)
    # >>>[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

    # 是一个生成器(generator)，节省内存空间
    num2 = (i*2 for i in range(10))  # 把推导式的[]换成()就是生成式

    print(num2)
    # >>><generator object main.<locals>.<genexpr> at 0x7fc233d7f510>


if __name__ == '__main__':
    main()
