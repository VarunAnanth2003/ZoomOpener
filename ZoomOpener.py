import webbrowser
import json
import time
from threading import Timer
classDict = json.load(open('zoomdata.json'))
currentInfo = time.localtime(time.time())
allTimes = {"period":[], "time":[]}

Timer.cancel
print("\n" + "SCHEDULE:" + "\n" + "---------------")

for index, info in enumerate(classDict['classData']):
    newTime = time.mktime(time.struct_time((currentInfo.tm_year, currentInfo.tm_mon, currentInfo.tm_mday, info["timeStartHour"], info["timeStartMinute"], 0, currentInfo.tm_wday, currentInfo.tm_yday, currentInfo.tm_isdst)))
    wday = currentInfo.tm_wday
    if(newTime-time.time() < 0):
        newTime += 86400
    if(classDict["daysOnline"][time.localtime(newTime).tm_wday]):
        if(classDict['classActive'][index]):
            print(info["name"] + ((35-(len(info["name"]))) * " ") + " @ " + time.asctime(time.localtime(newTime)))
        else:
            print(info["name"] + ((35-(len(info["name"]))) * " ") + " @ " + "ASYNCHRONOUS")
        allTimes["time"].append(newTime)
        allTimes["period"].append(index)

print("---------------")
print("You have " + str(len(allTimes["time"])) + " upcoming classes" + "\n")

def executeZoom():
    leastTimeDiff = float("inf")
    for t in allTimes["time"]:
        if(abs(t-time.time()) < leastTimeDiff):
            leastTimeDiff = abs(t-time.time())
            currentPeriod = allTimes["period"][allTimes["time"].index(t)]
    if(classDict['classActive'][currentPeriod]): 
        print("Joining " + classDict['classData'][currentPeriod]["name"] + "...")
        webbrowser.open(classDict['classData'][currentPeriod]["link"], 2)

for t in allTimes["time"]: 
    timer = Timer(t-time.time(), executeZoom)
    timer.start()

if(len(allTimes) == 0):
    input('Press ENTER to exit')
