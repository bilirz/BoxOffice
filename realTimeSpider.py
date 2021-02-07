"""
@author 认真猫
@desc 一个使用requests库的猫眼专业版实时爬虫

true: 包含服务费
false: 不包含服务费
"""
import requests
import csv
import time
from requests.adapters import HTTPAdapter
from function import *

headers = {"User-Agent": randomAgent()}

session = requests.session()
session.mount("https://", HTTPAdapter(max_retries=3))


def getData(isSplit):
    json = session.get(
        f"http://piaofang.maoyan.com/getBoxList?date=1&isSplit={isSplit}",
        headers=headers,
    ).json()
    with open(
        f"./data/realTime/{isSplit}.csv", "a", encoding="utf-8-sig", newline=""
    ) as f:
        fCsv = csv.writer(f)
        for j in json["boxOffice"]["data"]["list"]:
            row = [
                # 电影的ID
                j["movieInfo"]["movieId"],
                # 电影的名字
                j["movieInfo"]["movieName"],
                # 电影上映多少天
                j["movieInfo"]["releaseInfo"],
                # 电影今日票房
                j["boxDesc"],
                # 电影今日票房占比
                j["boxRate"],
                # 电影的拍片占比
                j["seatCountRate"],
                # 电影的拍坐占比
                j["showCountRate"],
                # 电影的总票房
                j["sumBoxDesc"],
                # 当日电影总大盘
                f"{json['boxOffice']['data']['nationalBox']['num']}{json['boxOffice']['data']['nationalBox']['unit']}",
                # 爬取时间
                f"{json['boxOffice']['data']['updateInfo']['date']} {json['boxOffice']['data']['updateInfo']['time']}",
                # time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            ]
            fCsv.writerow(row)


while True:
    getData("true")
    getData("false")
    # 每10分钟爬取一次
    time.sleep(600)
