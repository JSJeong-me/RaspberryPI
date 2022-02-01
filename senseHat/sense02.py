import time
import datetime
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

try:
    while True:
        now = datetime.datetime.now()
        temp = sense.get_temperature()
        #print(now)
        f = open('temphumi.txt','a')
        f.write('{0} : {1} \r\n'.format(str(now),str(temp)))
        f.close()
        time.sleep(5.0)
    
except KeyboardInterrupt:
    pass