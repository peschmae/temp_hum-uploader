# Temperature & Humidity Uploader
# Deprecated!
## Adafruit Library no longer supported in favor of circuitpython libraries

Small script to be used on a Beaglebone Black (BBB) or Raspberry PI, which 
queries a DHT22 sensor, and POSTS the result to a REST API.  
To be used in conjunction with the temp_hum-rest-api I've written.  

Based on [Requests](http://docs.python-requests.org/en/master/) and the 
[Adafruit DHT Python Library](https://github.com/adafruit/Adafruit_Python_DHT)

## Usage
Setup the application in a virtualenv, using pip
```
virtualenv env  
pip install -r requirements.txt
```

Start the application
```
sudo <virtualenv>/bin/python temp_hum_uploader.py
```
## FAQ
* Why sudo?
> To read from GPIO the script needs to be executed as root or using sudo.

* What about configuration?
> Currently all the settings are set, in the script itself, but I'll probably
move them into a config.cfg sometime.
