# multiple Arguments in a Funciton

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)



c = average(4,6,7,9,0,10)
print (c)