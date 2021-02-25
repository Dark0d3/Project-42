import requests

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
    return times

def light(state):
    output = []
    for i in range(0,len(state)):
        if state[i] == 2:
            output.append('green')
        elif state[i] == 1:
            output.append('yellow')
        else:
            output.append('red')
    print("Pole 1 light : " + str(output[0]))
    print("Pole 2 light : " + str(output[1]))
    print("Pole 3 light : " + str(output[2]))
    print("Pole 4 light : " + str(output[3]))
    #print(output)