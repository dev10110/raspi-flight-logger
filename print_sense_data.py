from sense_hat import SenseHat
import datetime
from csv import writer
import csv
import time
import os



sense = SenseHat()

sense.show_letter('*')

event = sense.stick.wait_for_event()

sense.show_message("!")



def get_sense_data():
    current_time = datetime.datetime.now()
    duration=current_time-start_time
    sense_data = []
    sense_data.append(duration.total_seconds())
    
    accel = sense.get_accelerometer_raw()
    sense_data.append(accel["x"])
    sense_data.append(accel["y"])
    sense_data.append(accel["z"])
    
    sense_data.append(sense.get_temperature())
    sense_data.append(sense.get_pressure())
    sense_data.append(sense.get_humidity())

    orientation = sense.get_orientation()
    sense_data.append(orientation["roll"])
    sense_data.append(orientation["pitch"])
    sense_data.append(orientation["yaw"])

    gyro = sense.get_gyroscope_raw()
    sense_data.append(gyro["x"])
    sense_data.append(gyro["y"])
    sense_data.append(gyro["z"])





    compass = sense.get_compass_raw()
    sense_data.append(compass["x"])
    sense_data.append(compass["y"])
    sense_data.append(compass["z"])

    #print(sense_data)
    
    return sense_data

filelocation = '/home/pi/Desktop/sensehat_data/'
timestring = time.strftime("%Y_%m_%d-%H_%M_%S")
filename = filelocation + 'data_'+  timestring + '.csv'
#sense.show_message("F: ")
sense.show_message(timestring)
n=0
timestamp=0
delaytime=0.005

start_time=datetime.datetime.now()

with open(filename,'a+',newline='',buffering = 1) as f:
    data_writer =writer(f)
    data_writer.writerow([time.strftime("%Y_%m_%d"),time.strftime("%H_%M_%S")])
    data_writer.writerow(['t','ax','ay','az','temp','P','hum','roll','pitch','yaw','gx','gy','gz','cx','cy','cz'])

    while True:
        data = get_sense_data()
        if data[0]-timestamp>delaytime:
            timestamp=data[0]
            data_writer.writerow(data)
            n += 1
            for i in range(8):
                if n%8==i:
                    sense.set_pixel(i,0,(255,0,0))
                else:
                    sense.set_pixel(i,0,(0,0,0))
                
