import os
import glob
import time
import sys
import urllib2
from time import sleep

# Enter Your API key here
myAPI = 'BD5TBMBWWWX6Q1VP' 
# URL where we will send the data, Don't change it
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
	f = open(device_file, 'r')
	lines = f.readlines()
	f.close()
	return lines

def read_temp():
	lines = read_temp_raw()
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(8)
		lines = read_temp_raw()
	equals_pos = lines[1].find('t=')
	if equals_pos != -1:
		temp_string = lines[1][equals_pos+2:]
		temp_c = float(temp_string) / 1000.0
		temp_f = temp_c * 9.0 / 5.0 + 32.0
		return temp_c, temp_f
		
	

while True:
	temp_c, temp_f = read_temp()
	
	# Sending the data to thingspeak
	url = baseURL + '&field1=%s' % (temp_c)
	print (url)
	conn = urllib2.urlopen(url)
	print conn.read()
	# Closing the connection
	conn.close()
	
	time.sleep(8)
