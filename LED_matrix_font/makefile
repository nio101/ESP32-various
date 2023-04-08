.DEFAULT_GOAL := mydefault
.ONESHELL:


all_files= boot.py main.py m_ntptime.py m_urequests.py
core_files= main.py

send_all:
	@/bin/echo -e "\x1B[01;93m -= Sending all source code files to flash fs  =- \x1B[0m"
	@sleep 1
	$(foreach file,$(all_files), ampy -p /dev/ttyUSB0 put $(file);)
	#ampy -p /dev/ttyUSB0 reset

send:
	@/bin/echo -e "\x1B[01;93m -= Sending core source code files to flash fs =- \x1B[0m"
	@sleep 1
	$(foreach file,$(core_files), ampy -p /dev/ttyUSB0 put $(file);)
	#ampy -p /dev/ttyUSB0 reset

repl:
	@/bin/echo -e "\x1B[01;93m -= Entering REPL (CTRL-a then k then y to quit) =- \x1B[0m"
	@sleep 1
	sudo screen /dev/ttyUSB0 115200

run: send repl

mydefault:
	@/bin/echo -e "try: send_all, send, repl, run"

.PHONY: send_all send repl run
