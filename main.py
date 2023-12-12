import time

from scraper import scraper
from hot import hot

while True:
    try:
        hot()
        print(f"获取热门视频成功，开始爬取视频信息，当前时间为{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}")
        scraper()
        print(f"爬取完成，休息一小时，下次爬取将在{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 3600))}开始")
        time.sleep(3600)
    except Exception as e:
        print(f"出现错误：{e}")
        time.sleep(3600)