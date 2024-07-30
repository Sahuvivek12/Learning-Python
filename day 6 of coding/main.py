box = [1,9,88,7,65,34,2,3,5]

box.append(7)
box.reverse
box.sort(reverse=True)
m = box.copy
box.insert(3, 899)
m = [900,1000,1100]
box.extend(m)

print(len(box))

print(box)