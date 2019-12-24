import os, sys, time
import qwiic

# Connect to Mux
mux = qwiic.QwiicTCA9548A()
# Initially Disable All Channels
frontAddress = input("Select the front sensor address: ")
frontToF = qwiic.QwiicVL53L1X(frontAddress)
rearAddress = input("Select the rear sensor address: ")
rearToF = qwiic.QwiicVL53L1X(rearAddress)

try:
    frontToF.SensorInit()
    rearToF.SensorInit()
except Exception as e:
    print(e)

while True:
    try:
        frontToF.StartRanging()						 # Write configuration bytes to initiate measurement
        rearToF.StartRanging()	
        time.sleep(.005)
        frontDistance = frontToF.GetDistance()	 # Get the result of the measurement from the sensor
        rearDistance = rearToF.GetDistance()
        time.sleep(.005)
        frontToF.StopRanging()
        rearToF.StopRanging()

        print("Front: %s | Rear: %s" % (frontDistance, rearDistance))

    except Exception as e:
        print(e)
