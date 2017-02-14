import datetime
import os
import todo_helper
import subprocess

now = datetime.datetime.now()
today = '{:04}{:02}{:02}.txt'.format(now.year, now.month, now.day)
yestDate = datetime.date.today()-datetime.timedelta(1)
yest = '{:04}{:02}{:02}.txt'.format(yestDate.year, yestDate.month, yestDate.day)

if os.path.exists(today):
  todo_helper.do_cleanup(today)
else:
  todo_helper.do_copy(yest, today)


