# Daylight Saving Time
# used to compute UTC offset depending on date
# settings used for France

# UTC_OFFSET = -4 * 60 * 60   # change the '-4' according to your timezone
# actual_time = time.localtime(time.time() + UTC_OFFSET)

import time
import datetime

def compute_UTC_offset():
    global UTC_OFFSET
    # year, month, day, hour, minute, second, weekday, day of the year, daylight saving
    today = datetime.date.today()
    #today = datetime.date(2023, 06, 01)
    #print('today is:',today)

    # find out the last sunday of march & october for the current year
    last_march = datetime.date(today.year, 3, 31)
    idx = (last_march.weekday() + 1) % 7 # MON = 0, SUN = 6 -> SUN = 0 .. SAT = 6
    last_sunday_march = last_march - datetime.timedelta(idx)

    last_october = datetime.date(today.year, 10, 31)
    idx = (last_october.weekday() + 1) % 7 # MON = 0, SUN = 6 -> SUN = 0 .. SAT = 6
    last_sunday_october = last_october - datetime.timedelta(idx)

    # if date >= last_sunday_march AND date < last_sunday_october => summer daylight saving time => UTC+2
    # ELSE winter daylight saving time => UTC+1

    if (today >= last_sunday_march) and (today < last_sunday_october):
        # summer : UTC+2
        UTC_OFFSET = +2 * 60 * 60
    else:
        # winter : UTC+1
        UTC_OFFSET = +1 * 60 * 60
    return UTC_OFFSET

def localtime_to_string(t):
    Dyear, Dmonth, Dday, Dhour, Dmin, Dsec, Dweekday, Dyearday = (t)
    dateformat = "{:02d}/{:02d}/{} {:02d}:{:02d}"
    return dateformat.format(Dday, Dmonth, Dyear, Dhour, Dmin,)

def actual_now():
    global UTC_OFFSET
    return time.localtime(time.time() + UTC_OFFSET)

