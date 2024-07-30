# File IO in python

# f = open('day 13 of coding/mytext.txt','r')
# text = f.read()               
# print(text)                                      #Reading a file
# f.close()



# f = open('day 13 of coding/mytext.txt','w')
# f.write("Hello World")                           #Writing in a file
# f.close()


# f = open('day 13 of coding/mytext.txt','a')
# f.write("Hello World")                           #Appending the value in a file
# f.close()


with open('day 13 of coding/mytext.txt','a') as f:
    f.write("\nPrinted from within the with block")