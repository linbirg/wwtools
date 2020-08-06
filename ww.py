## 打印指定日期是一年中的第几周，默认当前日期

import datetime
import sys


def print_ww(tday=None):
    if tday is None:
        tday = datetime.datetime.now()

    year, ww, wday = tday.isocalendar()
    print("当前", tday, "是", year, "年第", ww, "周 星期", wday)


def parse_ymd(s):
    year_s, mon_s, day_s = s.split('/')
    return datetime.datetime(int(year_s), int(mon_s), int(day_s))


if __name__ == '__main__':
    tday = None
    if len(list(sys.argv)) > 1:
        tday = parse_ymd(sys.argv[1])
    print_ww(tday)