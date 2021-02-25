import lightcontrol_pc_only as lightcontrol
#import lightcontrol
#----->Comment the first line and uncomment the second line if the code is executed on a Raspberry Pi<----#
import time
import veh_det

state = [0,0,0,0]
vehicles = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
timeWeights = [0, 0, 0, 0]
j=0
ways = 4
maxlim = 120
frame_seq = 0
while j<2:
    time_length = 240.0
    fps=30
    #total frames = 7200
    if(frame_seq >= 7200):
         break
    
    j=j+1  
    for i in range(0,ways):
        frame_seq = frame_seq + 60
        frame_no = (frame_seq /(time_length*fps)) 
        waydata=veh_det.getVehs(frame_seq)
        timeWeights[0] = waydata[0][0] + (waydata[0][1]*3) + waydata[0][2]
        timeWeights[1] = waydata[1][0] + (waydata[1][1]*3) + waydata[1][2]
        timeWeights[2] = waydata[2][0] + (waydata[2][1]*3) + waydata[2][2]
        timeWeights[3] = waydata[3][0] + (waydata[3][1]*3) + waydata[3][2]
        
        totveh = waydata[4]
        totwei = waydata[5]
        print("totveh = " + str(totveh))
        print("totwei = " + str(totwei))
        if(totwei < 30):
             maxlim = 30
        elif(totwei < 60):
             maxlim=60
        else:
             maxlim=120
        print("maxlim =" + str(maxlim))
        
        if(totveh > 0):
             print("timeweights : " + str(timeWeights))
             retime = lightcontrol.control(timeWeights, totwei, maxlim)
             state[i] = 2
             lightcontrol.light(state)
             time.sleep(retime[i])
             timeWeights[i]=timeWeights[i]-(retime[i]*totwei/maxlim)
             state[i] = 1
             lightcontrol.light(state)
             if retime[i] == 0:
                 time.sleep(0)
             else:
                 time.sleep(3)
             state[i] = 0
             lightcontrol.light(state)     
        else:
             state = [3, 3, 3, 3]
             lightcontrol.light(state)

