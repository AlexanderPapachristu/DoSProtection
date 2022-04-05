IP = "not set"
Time = 0
dict2 = {
'10.0.2.1': [7, 10, 10, False, 5, 35],
'10.0.2.2': [7, 11, 10, False, 5, 35],
'10.0.2.3': [7, 12, 10, False, 5, 35],
} #AVGTime, LastPacket, Threshold, Flag, Packets Recieved, running sum of packet times
while IP != "exit":
    print("Enter IP")
    IP = input()
    if IP in dict2:
        if dict2[IP][3]: # if IP was flagged to be malicious
            print("Packet denied access")
        else:
            print("Enter Packet Time")
            Time = input()
            Time = int(Time)
            if (Time - dict2.get(IP)[1]) > dict2.get(IP)[2]: # test if packet time is over Threshold
                print("Over Threshold")
                dict2[IP][3] = False
            else:
                print("Packet Bad")
                dict2[IP][3] = True

            if dict2[IP][4] < 5:
                dict2[IP][4] += 1 #update packet counter
                dict2[IP][5] = (Time-dict2[IP][1]) # add to running sum
                dict2[IP][1] = Time
                dict2[IP][0] = dict2[IP][5]/dict2[IP][4] # get new average packet time
            elif dict2[IP][4] == 5:
                dict2[IP][2] = dict2[IP][1]/5 #create threshold for new data based on average time to send packet

    else:
        dict2[IP] =  [Time,Time,5,False, 1, Time]


#When flag is true, don't let packet through
