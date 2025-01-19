import time

is_light_on = input("Is light on? (y/n): ") 

if is_light_on.lower() == "y": 
    print("light is on!")
else:
    print("light is off!")

time.sleep(0.3)

print("closing in one second!")
time.sleep(1)