today="/Users/$USER/todo/"$(date +%Y%m%d).txt
yest="/Users/$USER/todo/"$(date --date="-1 days" +%Y%m%d).txt
if [ -f $today ]
then
  echo "file exists"
  python3 todo.py --clean --file $today
  vim "$today"
else
  echo "file does not exist"
  python3 todo.py --copy --today $today --yest $yest
  vim "$today"
fi

