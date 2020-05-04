import time
import ds18b20
from ds18b20 import ds

sensor=ds() #creates sensor object set to default pin 2, units in Celcius, resolution 12 bit
#same result from sensor=ds(2,'c',12)
#sensor.addr, sensor.pin, sensor.unit, and sensor.res values are now available
#you can change the object parameters by the following:
#pin number - sensor.pin=[number]
#unit - sensor.unit=['c'|'f']
#resolution - sensor.res=[9|10|11|12]

while True:
    temp=ds18b20.read(sensor) # a time.sleep is builtin to the function to allow time to take the reading
    #the builtin time.sleep is currently set to 1 second for all resolutions but will eventually
    #take less time for the lower resolutions once it has been added to the library
    print (temp)
    time.sleep(2)

