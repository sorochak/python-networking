

#!/usr/bin/python

import RPi.GPIO as GPIO
import sys
import temperature
import time

YELLOW = 27
RED = 18
GREEN = 22
temp = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)


#
# Replace the blank below with your device file
#
DEVICE_FILE = "/sys/devices/w1_bus_master1/10-00080326f4d3/w1_slave"
myFile = "temperature_file"

HTML_START = """
<html>
<head>
	<meta http-equiv="refresh" content="5">
	<title>Current Temperature</title>
</head>
<body>
"""

HTML_END = """
</body>
</html>
"""

# Write 'temp' to the file called "file_name"
def write_temp(temp, file_name):
	f = open(file_name, "w")
	f.write(str(temp))
	f.close()

# Return the value contained in the file called "file_name"
def read_temp(file_name):
	f = open(file_name, "r")
	temp = f.read()
	f.close()
	return float(temp)



def application(env, start_response):
	status = "200 OK"

	headers = [("Content-type", "text/html; charset=utf-8")]
	start_response(status, headers)

	body = [HTML_START]

	try:
		temp = temperature.read_temp(DEVICE_FILE)
		previous_temp = read_temp(myFile)
		write_temp(temp,myFile)


		body.append("It is currently " + str(temp) + "&degC\n")
		if (temp < previous_temp):
			body.append("temperature is falling")
			GPIO.output(GREEN, 1)
			GPIO.output(RED, 0)
			GPIO.output(YELLOW, 0)
		elif (temp > previous_temp):
			body.append("temperature is rising")
			GPIO.output(GREEN,0 )
            GPIO.output(RED, 1)
            GPIO.output(YELLOW, 0)
		else:
			body.append("temperature is constant")
            GPIO.output(GREEN,0 )
            GPIO.output(RED, 0)
            GPIO.output(YELLOW, 1)
	except Exception, details:
		sys.stdout.write(str(details))
		body.append("Error\n")
	finally:
		body.append(HTML_END)


	return body
