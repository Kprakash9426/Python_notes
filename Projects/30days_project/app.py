# 👉 “Bring the time module so I can use time-related functions.”
import time

# 👉 “Tell me the current time in Hours:Minutes format.”
# print() shows it on the screen.
print(time.strftime("%H:%M"))  #14:30

# asks the user:
# 👉 “Please type the alarm time in HH:MM (like 07:10 or 18:45).”

alarm_time = input("Enter the alarm time (HH:MM): ")

# Keep repeating until the current time matches the alarm time.”
# As long as current time IS NOT equal to the alarm time, the loop runs.

while time.strftime("%H:%M") != alarm_time:
      time.sleep(1) # “Wait for 1 second.,,So the program doesn’t check time thousands of times per second.”
print("Time to wake up!")