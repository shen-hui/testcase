import wget, tarfile
import os
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
# 删除下载文件
os.remove(out_fname)
