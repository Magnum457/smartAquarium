# imports
import os
import glob
import time

def setup():
    # configurando os dispositivos one-wire
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')

    # buscando os dispositivos one-wire
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'
    return device_file

# função que recupera a temperatura do sensor
def read_temp_raw():
    device_file = setup()
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

# função que formata os dados recuperados para celcius e farenheit
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

# loop
def loop_temp():
	return read_temp()	
	time.sleep(1)
