import configparser


config = configparser.ConfigParser()
config.read(filename='config.ini')
print("SSID:", config.get('wifi', 'SSID'))
config.read(filename='config.ini.pass')
print("passwd:", config.get('wifi', 'passwd'))

print("done")
