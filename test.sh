echo starting to run wget...
/etc/init.d/atd start
nohup at 14:59 <<< "mkdir /tmp/test" >/tmp/log.txt 2>&1 &

#python /tmp/testcase/test1.py 
#nohup python -u /tmp/testcase/test1.py >/tmp/log.txt 2>&1 &
