
'''
        Raspberry Pi GPIO Status and Control
'''
import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#define actuators GPIOs
ledRed = 18

#initialize GPIO status variables
ledRedSts = 0

# Define led pins as output
GPIO.setup(ledRed, GPIO.OUT)

# turn leds OFF
GPIO.output(ledRed, GPIO.LOW)


@app.route("/")

@app.route("/<deviceName>/<action>")
def action(deviceName, action):
        if deviceName == 'KIC':
                actuator = ledRed


        if action == "on":
                GPIO.output(actuator, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(actuator, GPIO.LOW)
                action = "off"


        ledRedSts = GPIO.input(ledRed)


        templateData = {
              'KIC'  : ledRedSts,

        }
        return render_template('index.html', **templateData)
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)