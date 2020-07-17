class ModelMetaclass(type):
    def __new__(cls, cls_name, parent_cls_name, attrs):
        mappings = dict()

        for k, v in attrs.items():
            # 判断是否是指定的StringField或者IntegerField的对象实例
            if isinstance(v, tuple):
                mappings[k] = v  # 把所有字段保存到字典

        # 删除属性
        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mapping__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = cls_name  # 假设表名和类名一样

        return type.__new__(cls, cls_name, parent_cls_name, attrs)


# 父类处理
class Model(object, metaclass=ModelMetaclass):

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def save(self):
        fields = list()
        args = list()

        for k, v in self.__mapping__.items():
            fields.append(v[0])
            args.append(getattr(self, k, None))

        # 数字、字符串引号处理
        args_temp = list()
        for temp in args:
            if isinstance(temp, int):
                args_temp.append(str(temp))
            elif isinstance(temp, str):
                args_temp.append("""'%s'""" % temp)
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(args_temp))

        print('SQL: %s' % sql)


# 子类简单定义
class User(Model):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")


u = User(uid=123456, name='Michael', email='test@gmail.com', password='my-pwd')
u.save()
