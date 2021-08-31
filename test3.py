import datetime
import threading
import wget, tarfile
import os


def func():
  print("haha")
  #如果需要循环调用，就要添加以下方法
  timer = threading.Timer(86400, func)
  timer.start()

# 获取现在时间
now_time = datetime.datetime.now()
# 获取明天时间
next_time = now_time + datetime.timedelta(days=+1)
next_year = next_time.date().year
next_month = next_time.date().month
next_day = next_time.date().day
# 获取明天3点时间
next_time = datetime.datetime.strptime(str(next_year)+"-"+str(next_month)+"-"+str(next_day)+" 13:00:00", "%Y-%m-%d %H:%M:%S")
# # 获取昨天时间
# last_time = now_time + datetime.timedelta(days=-1)

# 获取距离明天3点时间，单位为秒
timer_start_time = (next_time - now_time).total_seconds()
print(timer_start_time)
DATA_URL = 'http://www.robots.ox.ac.uk/~ankush/data.tar.gz'
# 本地硬盘文件
# DATA_URL = '/home/xxx/book/data.tar.gz'
out_fname = 'abc.tar.gz'
wget.download(DATA_URL, out=out_fname)
# 提取压缩包
tar = tarfile.open(out_fname)
tar.extractall()
tar.close()
# 删除下载文件
os.remove(out_fname)
# 54186.75975


#定时器,参数为(多少时间后执行，单位为秒，执行的方法)
timer = threading.Timer(timer_start_time, func)
timer.start()
