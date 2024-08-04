# a program to rename .png files in a folder 'Clear-The-Clutter'

import os
path = 'day 18 of coding/png/'
files = os.listdir(path)


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index+1), '.png'])))

# done