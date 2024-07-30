# For loop with else

# for i in range (5):

# i = 0
# while i<7:
#     i = i + 1
#     print("iteration number {}".format(i+1))

# else:
#     print("Loop has been executed successfully")

i = 0
while i<7:
    i = i + 1
    print("iteration number {}".format(i))
    if i == 4:
        break

else:
    print("Loop has been executed successfully")