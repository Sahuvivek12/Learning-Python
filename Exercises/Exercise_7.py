# a program to rename .png files in a folder 'Clear-The-Clutter'

import os
path = 'day 18 of coding/png/'
files = os.listdir(path)

i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"day 18 of coding/png/{file}", f"day 18 of coding/png/{i}.png")
        i = i+1

#done