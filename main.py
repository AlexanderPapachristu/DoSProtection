dict = {
'IP': ['10.0.2.1', '10.0.2.2', '10.0.2.3'],
'AVGTime': ['7', '7', '7'],
'LastPacket': ['10', '11', '12'],
'Threshold': [10, 10, 10]}
print(dict)

dict2 = {
'10.0.2.1': [7, 10, 10, False],
'10.0.2.2': [7, 11, 10, False],
'10.0.2.3': [7, 12, 10, False],
} #AVGTime, LastPacket, Threshold, Flag

IP = input()
Time = input()
Time = int(Time)

if (Time - dict2.get(IP)[1]) > dict2.get(IP)[2]:
    print("Over Threshold")
    dict2[IP][3] = False
else:
    print("Packet Bad")
    dict2[IP][3] = True

print(dict2)

#When flag is true, don't let packet through 
