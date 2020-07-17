import logging


"""
日志级别：
1.DEBUG (详细的信息，通常只出现在诊断问题上)
2.INFO (确认一切按预期进行)
3.WARNING (意想不到的事情发生了，这个软件还能按照预期进行。例如：磁盘空间低)
4.ERROR (更严重的问题，软件没能执行一些功能)
5.CRITICAL (一个严重的错误，表面程序本身无法继续运行)
"""

# 使用logging功能(默认是WARNING级别，DEBUG和INFO不会显示)

# logging.basicConfig(level=logging.DEBUG)  # 把级别设置成DEBUG就能显示所有日志信息

# 格式化输出日志信息，将日志文件保存为log.txt文件，a是追加，w是覆盖
logging.basicConfig(level=logging.DEBUG, filename="./log.txt", filemode="a", format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")

logging.debug('logging-debug message')
logging.info('logging-info message')
logging.warning('logging-warning message')
logging.error('logging-info message')
logging.critical('logging-critical message')
