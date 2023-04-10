import machine
import micropython


rtc = machine.RTC()

now = daylightsavingtime.actual_now()
print('now is', daylightsavingtime.localtime_to_string(now))

rtc.alarm(0,10000,repeat=True)

print('ok')