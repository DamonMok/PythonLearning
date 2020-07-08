
class Goods(object):

    def __init__(self):
        self.original_price = 100

    def get_price(self):
        return self.original_price * 0.9

    def set_price(self, value):
        self.original_price = value

    def del_price(self):
        del self.original_price

    # 调用类属性时，根据getter/setter/deleter/__doc__来判断调用哪个方法
    PRICE = property(get_price, set_price, del_price, "this is description")


def main():
    # getter
    goods = Goods()
    print(goods.PRICE)

    # setter
    goods.PRICE = 200
    print(goods.PRICE)

    # __doc__
    print(Goods.PRICE.__doc__)

    # deleter
    del goods.PRICE


if __name__ == '__main__':
    main()
