# Dictionary methods in python


employee_senior = {122: 66, 44:55, 66:7, 88:9}
employee_junior = {33:24, 66:78}

employee_senior.update(employee_junior)
print(employee_senior)

employee_junior.clear()
print(employee_junior)

employee_senior.pop(122)
print(employee_senior)
