#Good-Morning-Sir

import time

timestamp1 = int(time.strftime('%H'))

if ((timestamp1)>=0 and (timestamp1)<12):
    print("Good Morning")
elif((timestamp1)>=12 and (timestamp1)<16):
    print("Good Afternoon")
elif((timestamp1)>=16 and (timestamp1)<19):
    print("Good evening")
elif((timestamp1)>=19 and (timestamp1)<24):
    print("Good night")