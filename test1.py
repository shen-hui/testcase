import time,os,sched

import wget, tarfile
import os

schedule = sched.scheduler(time.time,time.sleep)
def perform_command(cmd,inc):
  os.system(cmd)
  print('task')
def timming_exe(cmd,inc=60):
  schedule.enter(inc,0,perform_command,(cmd,inc))
  # 网络地址
  DATA_URL = 'http://www.robots.ox.ac.uk/~ankush/data.tar.gz'
  # 本地硬盘文件
  # DATA_URL = '/home/xxx/book/data.tar.gz'
  out_fname = 'abc.tar.gz'
  wget.download(DATA_URL, out=out_fname)
  # 提取压缩包
  tar = tarfile.open(out_fname)
  tar.extractall()
  tar.close()
  schedule.run()
print('show time after 20 seconds:')
timming_exe('echo %time%',120)
