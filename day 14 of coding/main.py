f = open('day 14 of coding/mytext.txt','r')

while True:
    line = f.readlines()
    if not line:
        break
    print(line)