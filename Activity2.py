import calendar 
cal=calendar.Calendar()
for x in cal.itermonthdates(2026,3):
    print(x)