#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import csv
import time
from datetime import datetime
import mysql.connector

#connecting to local DB
mydb = mysql.connector.connect( 
  host="localhost",
  user="rishabh",
  passwd="123456",
  database="power"
)

mycursor = mydb.cursor()


# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("current_sensor/device1")
  print (msg.payload.decode() )




def on_message(client, userdata, msg):
  print ((msg.payload.decode()) )
  #print(time.ctime())
  global rawvalue
  rawvalue = str(msg.payload.decode())
  
  # row = [time.ctime() ,int(msg.payload.decode())]
  # with open('sensor.csv', 'a') as csvFile:
  #   writer = csv.writer(csvFile)
  #   writer.writerow(row)

  # csvFile.close()
  dateTimeObj = datetime.now()
  datenow = dateTimeObj.strftime("%Y-%m-%d %H:%M:%S")
  #timenow = dateTimeObj.strftime("%H:%M:%S")

  sql = "INSERT INTO sensor (date, value) VALUES (%s, %s)"
  val = (datenow, rawvalue)
  mycursor.execute(sql, val)

  mydb.commit()
  #once data is recieved from ESP-8266, switch to websocket port so that website JS script can directly subscribe to it
  client= mqtt.Client("client-socks",transport='websockets')
  client.connect("192.168.43.88",9001)           
  client.publish("current_sensor/device1",rawvalue)
  client = mqtt.Client()
  #subscribe back to normal port
  client.connect("192.168.43.88",1883,60)
  



  

  

  
    
client = mqtt.Client()
client.connect("192.168.43.88",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
