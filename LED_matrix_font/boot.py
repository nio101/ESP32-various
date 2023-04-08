# boot.py

import esp
from machine import Pin, PWM, reset, reset_cause, DEEPSLEEP_RESET, deepsleep, reset
import network
import uos
import gc
import ntptime
import time
import utime
import configparser
import daylightsavingtime


def error(message, error_code):
    # error encountered!
    print(message)
    #global pwm_led
    #pwm_led.deinit()
    #pwm_led = PWM(Pin(5), freq=error_code, duty=1022)
    utime.sleep(30)
    reset()


def AP_create(ssid, password):
    ap = network.WLAN(network.AP_IF)
    ap.active(False)
    ap.active(True)
    ap.config(essid=ssid, authmode=network.AUTH_WPA_WPA2_PSK, password=password)
    while ap.active() == False:
      pass
    print('Connection successful')
    print(ap.ifconfig())


def wlan_connect(ssid, password, hostname):
    wlan = network.WLAN(network.STA_IF)
    if not wlan.active() or not wlan.isconnected():
        wlan.active(False)
        wlan.active(True)
        if not wlan.active():
            error("**error trying to enable the WLAN**", 1)
        wlan.config(dhcp_hostname=hostname)
        """
        print('scanning wifi networks...')
        networks = wlan.scan()
        auth = ["(open)", "WEP", "WPA-PSK", "WPA2-PSK", "WPA/WPA2-PSK", "WPA2-ENTERPRISE"]
        for (t_ssid, t_bssid, t_channel, t_RSSI, t_authmode, t_hidden) in networks:
            print("\t{}: channel=={}, RSSI=={}, auth=={}, hidden=={}".format(t_ssid.decode("utf-8"), t_channel, t_RSSI, auth[t_authmode], t_hidden))
        """
        print('connecting to:', ssid, end='')
        wlan.connect(ssid, password)
        nb_sec_tries = 0
        while not wlan.isconnected():
            utime.sleep(1)
            print('.', end='')
            nb_sec_tries = nb_sec_tries + 1
            if nb_sec_tries == 10:
                error("** error trying to connect to the WIFI AP **", error_code=1)
            pass
        print("connected!")
        print('MAC address:',":".join(["{0:02x}".format(c) for c in wlan.config('mac')]))
        print('network config:', wlan.ifconfig())
    else:
        print("WLAN already connected!")
        print('MAC address:',":".join(["{0:02x}".format(c) for c in wlan.config('mac')]))
        print('network config:', wlan.ifconfig())


def fs_size():
    fs_stat = uos.statvfs('/')
    fs_size = fs_stat[0] * fs_stat[2]
    fs_free = fs_stat[0] * fs_stat[3]
    return "filesystem size: {0:0.1f}MB - free space: {0:0.1f}MB".format(fs_size/(1024*1024), fs_free/(1024*1024))


# boot
esp.osdebug(None)
gc.collect()
print()
print("=== boot.py ===")

# check if the device woke from a deep sleep
if reset_cause() == DEEPSLEEP_RESET:
    print('>> woke up from a deep sleep!')

config = configparser.ConfigParser()

config.read(filename='config.ini.pass')
password = config.get('wifi', 'passwd')

config.read(filename='config.ini')

wlan_connect(ssid=config.get('wifi', 'ssid'), password=password, hostname=config.get('wifi', 'hostname'))
#gragnague
#wlan_connect(ssid='Livebox-58A0', password='Zv5vFvXvxTvXFRb3z2', hostname='odin')
# ladern
#wlan_connect(ssid='Livebox-3586_MAISON', password='iWVNmv3fQS4c3nctAk', hostname='odin')
#AP_create(ssid='gazotron', password='13371337')
print(fs_size())

ntptime.timeout = 15
ntptime.settime()

daylightsavingtime.compute_UTC_offset()
now = daylightsavingtime.actual_now()
print('now is', daylightsavingtime.localtime_to_string(now))
