from pymysql import connect
import re
import urllib.parse


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


@route(r"/index.html")
def index(ret):
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
                <input type="button" value="添加" id="toAdd" name="toAdd" systemIdValue=%s>
            </td>
           </tr> 
        """

        for line_info in stock_info:
            html += tr_template % (line_info[0], line_info[1], line_info[2], line_info[3],
                                   line_info[4], line_info[5], line_info[6], line_info[7], line_info[1])

        content = re.sub("\{%content%\}", html, content)

        return content


@route(r"/center.html")
def center(ret):
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
                        <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
                    </td>
                    <td>
                        <input type="button" value="删除" id="toDel" name="toDel" systemIdValue=%s>
                    </td>
                </tr>
            """

        for line_info in stock_info:
            html += tr_template % (line_info[0], line_info[1], line_info[2], line_info[3],
                                   line_info[4], line_info[5], line_info[6], line_info[0], line_info[0])

        content = re.sub("\{%content%\}", html, content)

        return content


@route(r"/add/(\d+)\.html")
def add_focus(ret):
    """关注股票"""

    # 创建连接数据库
    conn = connect(host="localhost", port=3306, user="root", password="damonmok", database="stock_db")

    # 获取游标
    cursor = conn.cursor()

    # 1.获取股票代码
    stock_id = ret.group(1)

    # 2.判断是否有这个股票代码
    params = [stock_id]
    cursor.execute("""select * from info where code=%s""", params)

    if not cursor.fetchone():
        # 关闭游标和连接
        cursor.close()
        conn.close()
        return "没有该股票！"

    # 3.判断是否已经关注
    cursor.execute("""select * from info inner join focus on info.id=focus.info_id where  info.code=%s""", params)
    if cursor.fetchone():
        # 关闭游标和连接
        cursor.close()
        conn.close()
        return "已经关注过"

    # 4.添加关注
    cursor.execute("""insert into focus (info_id) select id from info where code=%s""", params)
    conn.commit()

    # 关闭游标和连接
    cursor.close()
    conn.close()

    return "关注成功！"


@route(r"/del/(\d+)\.html")
def del_focus(ret):
    """取消关注"""

    # 创建连接数据库
    conn = connect(host="localhost", port=3306, user="root", password="damonmok", database="stock_db")

    # 获取游标
    cursor = conn.cursor()

    # 1.获取股票代码
    stock_id = ret.group(1)

    # 2.判断是否有这个股票代码
    params = [stock_id]
    cursor.execute("""select * from info where code=%s""", params)

    if not cursor.fetchone():
        # 关闭游标和连接
        cursor.close()
        conn.close()
        return "没有该股票！"

    # 3.判断是否已经关注
    cursor.execute("""select * from info inner join focus on info.id=focus.info_id where  info.code=%s""", params)
    if not cursor.fetchone():
        # 关闭游标和连接
        cursor.close()
        conn.close()
        return "还没有关注该股票！"

    # 4.取消关注
    cursor.execute("""delete from focus where focus.info_id=(select id from info where code=%s)""", params)
    conn.commit()

    # 关闭游标和连接
    cursor.close()
    conn.close()

    return "取消关注成功！"


@route(r"/update/(\d+)\.html")
def show_update_page(ret):
    """显示更新页面"""

    # 创建连接数据库
    conn = connect(host="localhost", port=3306, user="root", password="damonmok", database="stock_db")

    # 获取游标
    cursor = conn.cursor()

    # 1.获取股票代码
    stock_id = ret.group(1)

    # 2.查找备注信息
    params = [stock_id]
    cursor.execute("""select note_info from focus where info_id=(select id from info where code=%s)""", params)

    note = cursor.fetchone()
    note_info = ""
    if note:
        note_info = note[0]

    # 1.获取股票代码
    stock_id = ret.group(1)

    with open("./templates/update.html", "r") as f:
        content = f.read()

        content = re.sub(r"\{%code%\}", stock_id, content)
        content = re.sub(r"\{%note_info%\}", note_info, content)

        return content


@route(r"/update/(\d+)/(.*)\.html")
def save_update_info(ret):
    """保存更新备注信息"""

    # 创建连接数据库
    conn = connect(host="localhost", port=3306, user="root", password="damonmok", database="stock_db")

    # 获取游标
    cursor = conn.cursor()

    # 1.获取修改的备注信息
    stock_code = ret.group(1)
    note_info = ret.group(2)  # 浏览器会将URL编码，发送给服务器，再发送给框架。如果URL有中文会进行编码，需要显示中文的话，这里需要解码
    note_info = urllib.parse.unquote(note_info)

    # 2.修改备注
    params = [note_info, stock_code]
    cursor.execute("""update focus set note_info=%s where info_id=(select id from info where code=%s)""", params)
    conn.commit()

    # 关闭游标和连接
    cursor.close()
    conn.close()

    return "修改备注成功！"


def application(environ, start_response):

    # 1.调用web服务器传过来的函数，给服务器返回header信息
    start_response('200 OK', [('Content-Type', 'text/html;charset="utf-8"')])

    # 2.给服务器返回body信息
    file_name = environ['PATH_INFO']

    try:
        for url, func in URL_FUNC_DICT.items():

            ret = re.match(url, file_name)
            if ret:
                return func(ret)

        return "请求的URL{%s}没有对应的函数" % file_name

    except Exception as ret:
        return "产生了异常：%s" % str(ret)
