import datetime
today=datetime.date.today()
print('Today:',today)

import time
timestamp=time.time()
print(timestamp)

yesterday=today-datetime.timedelta(days=1)
print('yesterday:',yesterday)

tomorrow=today+datetime.timedelta(days=1)
print('tomorrow:',tomorrow)

print('time between tomorrow and yesterday:' ,tomorrow-yesterday)


#print the whole year calender
import calendar
year=calendar.prcal(2023)
#print specific month
month=calendar.month(2023,2)
print('\n',month)
