import urllib.request
import gevent
from gevent import monkey


monkey.patch_all()


def downloader(img_name, img_url):
    """图片下载"""
    ret = urllib.request.urlopen(img_url)

    img_content = ret.read()

    with open(img_name, "wb") as f:
        f.write(img_content)


def main():

    # 在joinall里面创建gevent对象，这些对象就会等待执行完任务再结束
    # Wait for the ``greenlets`` to finish.
    gevent.joinall([
        gevent.spawn(downloader, "1.jpg", "http://p3.pstatp.com/origin/pgc-image/d3d675232043481599fe24a091918951"),
        gevent.spawn(downloader, "2.jpg", "http://p3.pstatp.com/origin/pgc-image/c6b27c33f7254e11ab3e19e5cb0a2464")
    ])


if __name__ == '__main__':
    main()
