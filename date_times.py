
from datetime import date
from datetime import time
from datetime import datetime

today = date.today()
print "Today's date is", today;
now = datetime.now()
print now.strftime("%a, %d %B, %Y"); #full date with century

print now.strftime("%H:%M");
