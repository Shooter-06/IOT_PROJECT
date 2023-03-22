from tkinter import *
import tkinter as tk
import adafruit_dht as dht
import threading
import tkFont
import ImageTk
import RPi.GPIO as GPIO

pin=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.OUT)

root = tk.Tk()

image = PhotoImage(file="background.gif")

background=Label(root, image=image)
background.place(x=0,y=0,relwidth=1, relheight=1)

temperature = StringVar()
temperature.set("----"+" °C")

humidity = StringVar()
humidity.set("----"+" %")

temperatureLabel = Label(root, fg="white", background="#00dbde", textvariable=temperature, font=("Helvetica", 40,"bold"))
temperatureLabel.place(x=580, y=100)

humidityLabel = Label(root, fg="white", background="#00dbde", textvariable=humidity, font=("Helvetica", 40,"bold"))
humidityLabel.place(x=580, y=200)
 
root.attributes("-fullscreen",True)
root.bind("<1>",exit)

def exit():
    root.quit()

def readSensor():
    root.after(2000, readSensor)
    h,t = dht.read_retry(dht.DHT22,20)
    temp = "%.1f" %t
    temperature.set(temp+" °C")
    hum = "%.1f" %h
    humidity.set(hum+"  %")

root.after(2000, readSensor)

root.mainloop()