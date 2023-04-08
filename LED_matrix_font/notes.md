TODO-list:
+ implement improved version of NTP : catch timeout and zero value returns (kiss of death)
	+ test it with bad WIFI passwd and too many/frequent ntp requests
+ during boot, if any problem/error (WAN, NTP) => fill in error info and flag
  + main.py will use this to indicate error on display, reboot/restart will be manual
