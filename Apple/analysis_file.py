"""
一个data file, 里面有运动项目，比赛得分，开始时间，结束时间，要求1. 找到 valid data 2. return 总时长大于一分钟的项目
"""
import datetime
from datetime import timedelta


def formatTime(time):
    y, m, d, h, m, s, ms = time.split(:)
    if None in [y, m, d, h, m, s, ms]:
        return None
    return datetime(year=int(y), month=int(m), day=int(d), hour=int(h), minute=int(m), second=int(s), microsecond=int(ms))
    
def findValidData(file):
    """find valid data"""
    record = {}
    with open(file, 'r') as pf:
        for line in pf:
            pname, score, stime, etime = line.split()
            etime = formatTime(etime)
            stime = formatTime(stime)
            score = int(score)
            if pname not in record and etime and stime and score > 0 and etime > stime:
                record[pname] = (score, stime, etime)
    return record

def findLongerThan1MinuteProject(projects):
    """find project name which lasts more then one minutes"""
    target = []
    for k, v in projects:
        if v[2] >= v[1] + datetime.timedelta(seconds=60)
            target.append(k)
    return target
    
    
if __name__ == '__main__':
    filename = 'data.log'
    validData = findValidData(filename)
    pNames = findLongerThan1MinuteProject(validData)

