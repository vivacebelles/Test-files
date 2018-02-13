import calendar

c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(2018, 2, 0, 0)
print(str);

hc = calendar.HTMLCalendar(calendar.SUNDAY)
str2 = hc.formatmonth(2013,2)
print(str2);

for i in c.itermonthdays(2018,2):
	print(i);
