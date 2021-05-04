import webbrowser
import json
import time
from threading import Timer
currentPeriod = 0
classDict = json.load(open('zoomdata.json'))
currentInfo = time.localtime(time.time())
allTimes = []

Timer.cancel
print("\n" + "SCHEDULE:" + "\n" + "---------------")
for index, info in enumerate(classDict['classData']):
    newTime = time.mktime(time.struct_time((currentInfo.tm_year, currentInfo.tm_mon, currentInfo.tm_mday, info["timeStartHour"], info["timeStartMinute"], 0, currentInfo.tm_wday, currentInfo.tm_yday, currentInfo.tm_isdst)))
    wday = currentInfo.tm_wday
    if(newTime-time.time() < 0):
        newTime += 86400
    if(classDict["daysOnline"][time.localtime(newTime).tm_wday]):
        if(classDict['classActive'][index]):
            allTimes.append(newTime-time.time())
            print(info["name"] + ((35-(len(info["name"]))) * " ") + " @ " + time.asctime(time.localtime(newTime)))
        else:
            print(info["name"] + ((35-(len(info["name"]))) * " ") + " @ " + "ASYNCHRONOUS")

print("---------------")
print("You have " + str(len(allTimes)) + " upcoming classes" + "\n")

def executeZoom():
    global currentPeriod
    print("Joining " + classDict['classData'][currentPeriod]["name"] + "...")
    webbrowser.open(classDict['classData'][currentPeriod]["link"], 2)
    currentPeriod = currentPeriod + 1
    if(currentPeriod == 7):
        input('Press ENTER to exit')

for period, t in enumerate(allTimes):
    timer = Timer(t, executeZoom)
    timer.start()

if(len(allTimes) == 0):
    input('Press ENTER to exit')
