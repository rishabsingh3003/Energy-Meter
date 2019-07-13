#include <ESP8266WiFi.h>                 // Necessary ESP - 8266 Wifi Library
#include <PubSubClient.h>              // For MQTT Protocol
#include "EmonLib.h"                   // Include Emon Library
EnergyMonitor emon1;                   // Create an instance




// use onboard LED for convenience 
#define LED (2)
// maximum received message length 
#define MAX_MSG_LEN (128)
// Wifi configuration
const char* ssid = "G4 PLAY";
const char* password = "55555555";
// MQTT Configuration
// if you have a hostname set for the MQTT server, you can use it here
const char *serverHostname = "192.168.43.88";                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             147);
// the topic we want to use
const char *topic = "test/message";
WiFiClient espClient;
PubSubClient client(espClient);

//int sensor() is called whenever a reading from the sensor is needed
int sensor(){
  
  
double Irms = emon1.calcIrms(1480);  // Calculate Irms only
  
  //Serial.print(Irms*220.0);         // Apparent power
  //Serial.print(" ");
  //Serial.println(Irms);    // Irms

return Irms;
  }


  
// connect to wifi
void connectWifi() {
  delay(10);
  // Connecting to a WiFi network
  Serial.printf("\nConnecting to %s\n", ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(250);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("WiFi connected on IP address ");
  Serial.println(WiFi.localIP());
}
// connect to a MQTT broker
void connectMQTT() {
  // Wait until we're connected
  while (!client.connected()) {
    // Create a random client ID
    String clientId = "ESP8266-";
    clientId += String(random(0xffff), HEX);
    Serial.printf("MQTT connecting as client %s...\n", clientId.c_str());
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("MQTT connected");
      // Once connected, publish an announcement...
      
      // ... and resubscribe
     // client.subscribe(topic);
    } else {
      Serial.printf("MQTT failed, state %s, retrying...\n", client.state());
      // Wait before retrying
      delay(2500);
    }
  }
}
//Callback function for MQTT

  void callback(char *topic, byte *payload, unsigned int length) {
  // copy payload to a static string
  static char message[MAX_MSG_LEN+1];
  if (length > MAX_MSG_LEN) {
    length = MAX_MSG_LEN;
  }
  strncpy(message, (char *)payload, length);
  message[length] = '\0';
  
  Serial.printf("topic %s, message received: %s\n", topic, message);

}


void setup() {
// LED pin as output
  pinMode(LED, OUTPUT);      
  digitalWrite(LED, HIGH);
  // Configure serial port for debugging
  Serial.begin(9600);
  // Initialise wifi connection - this will wait until connected
  connectWifi();
  // connect to MQTT server  
  client.setServer(serverHostname, 1883); //Initalize MQTT
  client.setCallback(callback);
  emon1.current(A0, 57 );             // Current: input pin, calibration.

}


void loop() {
  if (!client.connected()) {
      connectMQTT();
    }
    // this is ESSENTIAL!

     
    client.loop();
    // idle0
    double finalval=0;
    double avgval;
    for (int i = 0; i < 10; i++) {
      finalval = sensor()+finalval;     //take 10 values and average them out
      yield();
      }
      avgval=finalval/10;
  
    Serial.println(String(avgval).c_str());
    client.publish("current_sensor/device1", String(avgval).c_str(),true);  // publish data to MQTT broker

    delay(300);
    client.loop();

}
