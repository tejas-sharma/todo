import datetime
import os
import todo_helper
import subprocess
import argparse

now = datetime.datetime.now()
today = os.path.join(os.path.expanduser('~'),'todo','{:04}{:02}{:02}.txt'.format(now.year, now.month, now.day))
yestDate = datetime.date.today()-datetime.timedelta(1)
yest = os.path.join(os.path.expanduser('~'), 'todo', '{:04}{:02}{:02}.txt'.format(yestDate.year, yestDate.month, yestDate.day))

parser = argparse.ArgumentParser(description='todo utility')
parser.add_argument('config', help='path to config file')
args = parser.parse_args()

if not os.path.exists(args.config):
  open(args.config, 'w').close()

if os.path.exists(today):
  todo_helper.do_cleanup(today)
else:
  with open(args.config, 'r+') as f:
    configContents = list(f)
    if len(configContents) > 0 and os.path.exists(configContents[0].rstrip()):
      todo_helper.do_copy(configContents[0].rstrip(), today)
    f.seek(0)
    f.write(today+'\n')
