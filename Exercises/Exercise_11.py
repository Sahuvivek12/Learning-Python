# Exercise 11
# - Drink Water Reminder
# Write a python program which reminds you of drinking water every hour or two. 
# Your program can either beep or send desktop notifications for a specific operating system


import time
import plyer as p

running = True

while running:
    time.sleep(7200)
    p.notification.notify(
    title="Drink water reminder",
    message="Have a glass of water",
    timeout = 3)

    