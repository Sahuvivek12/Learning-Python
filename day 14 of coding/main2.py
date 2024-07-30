# Seek and tell functions in python

with open('day 14 of coding/mytext.txt', 'r')as f:
    f.seek(10)
    data = f.read()
    print(data)
