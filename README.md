# Raspi-flight-logger
Tools to be able to use the raspberry pi zero and the sense hat as a flight logger for a rocket flight.


Main script (called print_sense_data.py) runs on the rasp pi and allows the flight data to be logged directly into a csv file.

To help keep track of the files, we name the csv file using the date and time that the run began at. 
However since the raspi has no internal clock, if left unpowered for long without a wifi connection, it will forget the time. 

As such, I have the sequence of operations as:

1. Rasp pi starts
2. The ~/etc/rc.local has a command that runs the python scripts
3. A star is shown on the sense hat screen
4. The raspi waits for a joystick action.
5. Once found, the screen shows a '!'
6. The filename is shown on the screen
7. logging begins and a red dot scrolls across the screen to allow us to see that it is still working
8. the script keeps running until either killall python3 is executed or the raspi is shutdown

To ensure no data is lost, the data is saved to the file at every line (also useful incase the launch acceleration causes the script to fail)

Why did I not have it simply log from the beginning?

Mainly because it was difficult to keep track of when the script started, where it was being saved, and what time the rasp pi felt it was. As this would be used for rocket launches I wanted to be certain that the script was running before I placed it on the launchpad.




