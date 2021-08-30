import time,os,sched
schedule = sched.scheduler(time.time,time.sleep)
def perform_command(cmd,inc):
  os.system(cmd)
  print('task')
def timming_exe(cmd,inc=60):
  schedule.enter(inc,0,perform_command,(cmd,inc))
  schedule.run()
print('show time after 20 seconds:')
timming_exe('echo %time%',20)
