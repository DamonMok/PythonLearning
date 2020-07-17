import logging


"""
日志级别：
1.DEBUG (详细的信息，通常只出现在诊断问题上)
2.INFO (确认一切按预期进行)
3.WARNING (意想不到的事情发生了，这个软件还能按照预期进行。例如：磁盘空间低)
4.ERROR (更严重的问题，软件没能执行一些功能)
5.CRITICAL (一个严重的错误，表面程序本身无法继续运行)
"""

# 1.创建logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关

# 2.创建一个handler,用于写入日志文件
logfile = './log2.txt'
fh = logging.FileHandler(logfile, mode='w')  # 日志写入的方式：a为追加，w为覆盖
fh.setLevel(logging.DEBUG)  # 输出到文件的log等级开关

# 3.创建一个handler,用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)  # 输出到控制台的log等级开关

# 4.定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

# 日志
logging.debug('logging-debug message')
logging.info('logging-info message')
logging.warning('logging-warning message')
logging.error('logging-info message')
logging.critical('logging-critical message')
