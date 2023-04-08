import configparser


config = configparser.ConfigParser()
config.read(filename='config.ini')

config.add_section('mysql')

config.add_option('mysql', 'host')
config.add_option('mysql', 'user')
config.add_option('mysql', 'passwd')
config.add_option('mysql', 'db')

config.set('mysql', 'host', 'localhost')
config.set('mysql', 'user', 'user01')
config.set('mysql', 'passwd', 'mypass01wd')
config.set('mysql', 'db', 'sql-01')

config.write(filename='config.ini')

print("ok")
