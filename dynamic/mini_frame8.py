from pymysql import connect
import re


URL_FUNC_DICT = dict()

# 这个装饰器的功能只是用来在字典中添加类似"/index.html": index的键值对
# 其中index是方法的引用
# 到时候直接根据key调用方法，不会调用到call_func
def route(url):

    def set_func(func):
        URL_FUNC_DICT[url] = func

        def call_func():
            pass
        return call_func()
    return set_func


@route("/index.html")
def index():
    with open("./templates/index.html", "r") as f:
        content = f.read()

        # 使用MySQL展示数据
        # 1.创建连接数据库
        conn = connect(host="localhost", port=3306, user="root", password="damonmok", database="stock_db")

        # 2.获取游标
        cursor = conn.cursor()

        # 3.操作sql语句
        cursor.execute("""select * from info;""")

        # 4.获取数据
        stock_info = cursor.fetchall()  # 因为数据少，所以一次性获取。多的话要分页获取。

        # 5.关闭游标和连接
        cursor.close()
        conn.close()

        # 替换数据
        html = ""
        tr_template = """<tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <input type="button" value="添加" id="toAdd" name="toAdd" systemidvalue=%s>
            </td>
           </tr> 
        """

        for line_info in stock_info:
            html += tr_template % (line_info[0], line_info[1], line_info[2], line_info[3],
                                   line_info[4], line_info[5], line_info[6], line_info[7], line_info[0])

        content = re.sub("\{%content%\}", html, content)

        return content


@route("/center.html")
def center():
    with open("./templates/center.html", "r") as f:
        content = f.read()

        # 使用MySQL展示数据
        # 1.创建连接数据库
        conn = connect(host="localhost", port=3306, user="root", password="damonmok", database="stock_db")

        # 2.获取游标
        cursor = conn.cursor()

        # 3.操作sql语句
        cursor.execute("""select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info as i inner join 
                        focus as f on i.id=f.info_id;""")

        # 4.获取数据
        stock_info = cursor.fetchall()  # 因为数据少，所以一次性获取。多的话要分页获取。

        # 5.关闭游标和连接
        cursor.close()
        conn.close()

        # 替换数据
        html = ""
        tr_template = """
                <tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>
                        <a type="button" class="btn btn-default btn-xs" href="/update/300268.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
                    </td>
                    <td>
                        <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="300268">
                    </td>
                </tr>
            """

        for line_info in stock_info:
            html += tr_template % (line_info[0], line_info[1], line_info[2], line_info[3],
                                   line_info[4], line_info[5], line_info[6])

        content = re.sub("\{%content%\}", html, content)

        return content


def application(environ, start_response):

    # 1.调用web服务器传过来的函数，给服务器返回header信息
    start_response('200 OK', [('Content-Type', 'text/html;charset="utf-8"')])

    # 2.给服务器返回body信息
    file_name = environ['PATH_INFO']

    try:
        func = URL_FUNC_DICT[file_name]
        return func()
    except Exception as ret:
        return "产生了异常：%s" % str(ret)
