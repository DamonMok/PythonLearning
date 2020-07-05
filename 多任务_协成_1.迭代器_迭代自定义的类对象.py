from _collections_abc import Iterable, Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    # 类中如果有iter方法，就会变成可迭代Iteratle
    # 该方法返回一个可迭代器Iterator
    def __iter__(self):
        return ClassmateIterator(self)


class ClassmateIterator(object):
    def __init__(self, obj):
        self.obj = obj
        self.count = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.count < len(self.obj.names):
            ret = self.obj.names[self.count]
            self.count += 1
            return ret
        else:
            raise StopIteration


def main():
    """迭代自定义类对象"""
    c = Classmate()
    c.add("小明")
    c.add("小红")
    c.add("小芳")

    c_iterator = iter(c)

    print("判断Classmate对象是否为可迭代对象：%d" % isinstance(c, Iterable))
    print("判断可迭代对象中，iter方法返回的对象是迭代器：%d" % isinstance(c_iterator, Iterator))

    for name in c:
        print(name)


if __name__ == '__main__':
    main()
