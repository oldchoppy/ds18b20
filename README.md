# ds18b20
DS18B20 Library for MicroPython. I created this library to allow changing the resolution of the sensor. Right now, it works 
for one (1) sensor per pin and 9,10,11,12 bit resolutions. The delay is one second for all resolutions but I am working on
an update to increase the speed for lower resolutions.

## Installation

Same directory as main.py in your MicroPython application. This was tested using ESP8266 with MicroPython v1.12 firmware.

## Usage
example:
```python
import ds18b20
from ds18b20 import ds

sensor=ds()
#creates sensor object set to default pin 2, units in Celcius, resolution 12 bit
#same result from sensor=ds(2,'c',12)
#sensor.addr, sensor.pin, sensor.unit, and sensor.res values are now available
#you can change the object parameters by the following:
#pin number - sensor.pin=[number]
#unit - sensor.unit=['c'|'f']
#resolution - sensor.res=[9|10|11|12]

while True:
  temp=ds18b20.read(sensor) #this includes a 1 second delay for processing
  print(temp)
```
## License
[MIT](https://choosealicense.com/licenses/mit/)
