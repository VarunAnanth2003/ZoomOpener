# ZoomOpener
## Auto-Opener for Zoom classes
- Don't edit the python file, edit the JSON to your liking instead!
- To use: Simply run the `ZoomOpener.py` file with the `zoomdata.json` on the same directory level. Don't close the program until your last class opens.
### daysOnline field:
- Meant to map out which days classes are on. index 0 is Monday, to index 6 which is Sunday.
"true" means that class is there that day, "false" means that there is no class that day.
### classActive field:
- Meant to map out which classes meet on Zoom on any given day. The booleans parallel the classData
field. Period 1 is index 0, period 2 is index 1, etc. 
### classData field:
- Structured like so:

```
{
    "name": "[NAME OF CLASS]",
    "period": [PERIOD # OF CLASS],
    "link": "[ZOOM LINK]",
    "timeStartHour": [HOUR CLASS STARTS],
    "timeStartMinute": [MINUTE CLASS STARTS]
}
```

- Note that the "timeStartHour" and "timeStartMinute" fields should be in military time (0:00 - 23:59)

### Additional Notes:
- Using Windows Task Scheduler in tandem with a .bat file can automate this program further,
not requiring you to run the .py file every morning.

