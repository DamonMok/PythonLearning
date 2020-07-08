
class Goods(object):

    def __init__(self):
        self.original_price = 100

    @property
    def price(self):
        # 打九折
        return self.original_price * 0.9

    @price.setter
    def price(self, value):
        # 修改价格
        self.original_price = value

    @price.deleter
    def price(self):
        # 删除引用
        del self.original_price


def main():
    goods = Goods()
    print(goods.price)

    goods.price = 200
    print(goods.price)


if __name__ == '__main__':
    main()
