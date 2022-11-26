
'''
        Raspberry Pi GPIO Status and Control
'''
import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#definerer pin for komunikasjon med Arduino. 
out = 18

#definerer output til komunikasjonspinen aka out
strom = 0

# Setter pin 18 til output. Dette gjør at den sender signaler i stede for å lese av.
GPIO.setup(out, GPIO.OUT)

#setter output til lav, så KIC ikke kjører med en gang
GPIO.output(out, GPIO.LOW)


@app.route("/") 

@app.route("/<deviceName>/<action>") #lager variabler for nettsiden adressen
def action(deviceName, action):
        #sjekker om action  er on, dette er netttsiden en kommer til om en trykker knappen. Hvis ifsetningen er oppfylt så kjører koden.
        if action == "on":
                # setter output til høy i 1 sek for så å sette output til lav
                GPIO.output(out, GPIO.HIGH) 
                time.sleep(1)
                GPIO.output(out, GPIO.LOW)
                action = "off" 


        return render_template('index.html', **templateData)#går inn i mappen template og bruker filen index.html som html fil for nettsiden.

if __name__ == "__main__": 
   app.run(host='0.0.0.0', port=80, debug=True) #hoster serveren for pythonprogrammet og nettsiden.
