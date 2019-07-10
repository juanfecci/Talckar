import datetime, time
import signal
import sys

def signal_handler(sig, frame):
	print('\nYou pressed Ctrl+C!')
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:
	time.sleep(5)
	print(datetime.datetime.now()) 



'''
while True:
	time.sleep(5)
	print(datetime.datetime.now()) '''