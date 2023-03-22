from tkinter import *
import Adafruit_DHT as dht
import threading
import time
import smtplib
import RPi.GPIO as GPIO


# Define GPIO pin for the fan
fan_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(fan_pin, GPIO.OUT)

# Set up email notification
sender_email = '2070000@edu.vaniercollege.com' #change it
sender_password = '123456'
receiver_email = '2070000@edu.vaniercollege.com' #change it
smtp_server = 'smtp.gmail.com'
smtp_port = 587


def send_email(temp):
    # Create SMTP connection and log in
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls()
    server.login(sender_email, sender_password)

    # Send email
    message = 'Subject: Temperature Notification\n\nThe current temperature is {}. Would you like to turn on the fan?'.format(
        temp)
    server.sendmail(sender_email, receiver_email, message)

    # Close SMTP connection
    server.quit()


# Set up the DHT-11 sensor
sensor = dht.DHT11
pin = 4

while True:
    # Read temperature and humidity data from the sensor
    humidity, temperature = dht.read_retry(sensor, pin)

    # Check if data is valid
    if humidity is not None and temperature is not None:
        print('Temperature: {} C'.format(temperature))
        print('Humidity: {} %'.format(humidity))

        # Check if temperature exceeds the threshold
        if temperature > 24:
            # Send email notification and wait for user response
            send_email(temperature)
            user_response = input('Would you like to turn on the fan? (YES/NO): ')

            # Turn on the fan if user response is YES
            if user_response.upper() == 'YES':
                GPIO.output(fan_pin, GPIO.HIGH)
                print('Fan is turned on')
            else:
                print('Fan is not turned on')

        from DHT_sensors import humidity_temp_Dashboard
        
    else:
        print('Failed to retrieve data from the sensor')

    # Wait for 5 seconds before reading the sensor again
    time.sleep(5)

