# Project 42: ADAPTIVE TRAFFIC LIGHT ARCHITECTURE

Project 42 is an adaptive system that analyzes the traffic condition present at a given intersection in real time, and then determines the states of the traffic lights mounted in that intersection. The Project 42 system is self-sufficient enough to keep running even in adverse situations like an internet blackout.

The Project 42 architecture takes in the feeds from the cameras placed at the intersections. These feeds are used as sources for image processing and analysis. The total number of vehicles at each road is calculated. 

This is fed into an efficient algorithm, that calculates the inter-green time for each road connecting to the intersection.  Multiple factors such as the crossover time for a vehicle and terrain factors are also taken into consideration.

Since passenger vehicles like buses are to be given more priority, the architecture detects such vehicles and applies a larger weight to them, hence increasing the inter-green time for that road.

## Benefits 	
*	Eliminates idle wait. (Unlike the current system, signal will not be kept open for lanes with no vehicles.)
*	Reduction in the average waiting time will also reduce the percentage of traffic violations. (This will enhance the efficiency of commuting experience and also improves the fame of the department.)
*	Human intervention can be significantly reduced at the traffic signals. Officers may be assigned to report at the control rooms and they will have to manually intervene only for unexpected emergencies.
*	The system can also detect pedestrian behavior and can automatically respond accordingly.



## Initialization:
*	Write the latest raspbian OS in the SD card (Raspbian-Lite should suffice) (ref: https://www.raspberrypi.org/documentation/installation/installing-images/)
*	The code uses Rpi.GPIO instead of the new GPIO zero (make sure your os supports it)
*	Install python3 if it’s not pre-installed (ref: https://www.circuitbasics.com/how-to-write-and-run-a-python-program-on-the-raspberry-pi/)
*	Install Git (Ref: https://raspberrypi.stackexchange.com/questions/8658/can-i-install-git-on-raspbian)
*	Install opencv-python, cvlib, matplotlib, tensorflow, keras
*	Clone the project-42 repo (Run this in terminal: 
   $ git clone http://github.com/devgeetech/project-42 
*   If you are using video files as camera input, place the 4 video files in the root folder.
*   This repo is configured to use video files as camera input. To use actual camera feed, see veh_det.py and make the necessary updations specified in it.

## Raspberry Pi PIN Configuration:

*	The pin[] array (in lightcontrol.py) has the list of GPIOs (Physical naming convention). In the order as follows
    *	3: Light-Post1, Red
    *	5: Light-Post1, Yellow
    *	7: Light-Post1, Green
    *	8: Light-Post2, Red
    *	10: Light-Post2, Yellow
    *	11: Light-Post2, Green
    *	12: Light-Post3, Red
    *	13: Light-Post3, Yellow
    *	15: Light-Post3, Green
    *	16: Light-Post4, Red
    *	18: Light-Post4, Yellow
    *	19: Light-Post4, Green
*	You can configure it by changing the pin[] array accordingly
*	Connect the lights through relays or any required control circuitry according to the order given above. e.g. connect LED of traffic post 1 to PIN 3


##	References:
*	https://tutorials-raspberrypi.com/installing-opencv-on-the-raspberry-pi/
*	https://raspberrypi.stackexchange.com/questions/15420/how-to-install-python3-matplotlib-on-raspi/15457
*   https://towardsdatascience.com/count-number-of-cars-in-less-than-10-lines-of-code-using-python-40208b173554

## Running:
*	Run main.py in the project folder.
