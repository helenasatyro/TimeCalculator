def add_time(start, duration, wkday="noday"):
    curdayindex = 0
    isday = False
    wcounter = 0
    weirdos = {0:"AM", 1:"PM"}
    weekdays = {
        0:"monday", 
        1:"tuesday",
        2:"wednesday",
        3:"thursday",
        4:"friday",
        5:"saturday",
        6:"sunday",
        "noday":"noday"}
    if wkday != "noday":
        wkday = wkday.lower()
        curdayindex = list(weekdays.keys())[list(weekdays.values()).index(wkday)]
        isday = True
    start = start.split()
    ampm1 = start[1]
    ampm = ampm1
    starthour = int(start[0].split(":")[0])
  
    if ampm1 == "PM": 
        starthour += 12
       # wcounter = 1
    startmin = int(start[0].split(":")[1])
    #print(start, ampm, starthour, startmin)

    duration = duration.split(":")
    hours = int(duration[0])
    mins = int(duration[1])
    #print(duration, hours, mins)

    plushour = int((startmin+mins)/60)
    mins = (startmin + mins)%60
    days = int((hours+plushour+starthour)/24) 
    if isday: weekday = weekdays[days%7]
    hours = (hours+plushour+starthour)%24
    totalh = ((hours+plushour+starthour))
    curdayindex = (curdayindex + days)%7
    curday = ((weekdays.get(curdayindex)).title())
    
    count = starthour
    for hour in range(1,(plushour+hours)):
        count +=1
        if count == 12:
            count = 0
            wcounter +=1

        
    
    ampm = weirdos[wcounter%2]
    if hours == 24:
      hours = 0
      ampm = "AM"
      
    if 24 > hours > 12:
      hours -= 12
      ampm = "PM"
    if hours == 0:
      hours = 12
    
    if days == 1:
        days = " (next day)"
    elif days == 0:
        days = ""
    else:
        days = f" ({days} days later)"
    

    if isday:
        new_time = f"{(str(hours))}:{(str(mins)).zfill(2)} {ampm}, {curday}{days}"
    else:
        new_time = f"{(str(hours))}:{(str(mins)).zfill(2)} {ampm}{days}"
    #print(plushour)

    return new_time