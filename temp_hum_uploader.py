# import libraties used in script
import Adafruit_DHT
import requests
import urlparse
import time

# Type of sensor, can be Adafruit_DHT.DHT11, Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
DHT_TYPE = Adafruit_DHT.DHT22
 
# Sensor connected to Beaglebone Black pin P8_11
DHT_PIN  = 'P8_11'

REST_API_BASE = 'http://10.112.10.15:5000'
REST_API_ENDPOINT = '/temp-hum/'


while True:
    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(DHT_TYPE, DHT_PIN)

    # Note that sometimes you won't get a reading and
    # the results will be null (because Linux can't
    # guarantee the timing of calls to read the sensor).
    # If this happens try again!
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        try:
            r = requests.post(
                urlparse.urljoin(REST_API_BASE, REST_API_ENDPOINT),
                data={'temp': temperature, 'hum': humidity},
                timeout=30
            )
        except requests.exceptions.Timeout:
            print 'POST timed out after 30s'

    else:
        print('Failed to get reading. Try again!')

    time.sleep(60)
