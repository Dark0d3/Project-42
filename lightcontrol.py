import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

lightstate = [[1,0,0],[1,0,0],[1,0,0],[1,0,0]]
pin = [[3,5,7],[8,10,11],[12,13,15],[16,18,19]]

for i in range(0,len(pin)):
    for j in range(0,3):
        GPIO.setup(pin[i][j], GPIO.OUT, initial=GPIO.LOW)

def control(veh, totwei, maxlim):

    minlim = 0
    #avgtime = 6
    #lanes = 2
    terrainFactor = [1, 1, 1.5, 1]
    ways = len(veh) #no of lanes
    times = []
    time = 0
    for i in range(0,ways):
        pretime = ((veh[i]*terrainFactor[i])/totwei)*maxlim
        if(pretime%5 != 0):
             time = pretime + (5-(pretime%5))
        else:
             time=pretime
        if time>maxlim: 
            allotime = maxlim
        elif time<minlim:
            allotime=minlim
        else:
            allotime=time
        times.append(allotime)
    print(times)
    return times

def light(state):
    output = []
    for i in range(0,len(state)):
        if state[i] == 2:
            output.append('g')
            lightstate[i] = [0,0,1]
        elif state[i] == 1:
            output.append('y')
            lightstate[i] = [0,1,0]
        else:
            output.append('r')
            lightstate[i] = [1,0,0]
    print(output)
    setlight(lightstate,pin)

def setlight(listate,pino):
    for i in range(0,len(pino)):
        for j in range(0,3):
            if listate[i][j] == 1:
                GPIO.output(pino[i][j], GPIO.HIGH)
            else:
                GPIO.output(pino[i][j], GPIO.LOW)
                

def blink():
    lightstate = [[1,0,0],[0,1,0],[1,0,0],[0,1,0]]
    setlight(lightstate,pin)
    time.sleep(1)
    lightstate = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    setlight(lightstate,pin)
    time.sleep(1)