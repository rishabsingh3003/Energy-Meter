# Energy Meter
 This project uses a CT sensor and ESP8266 to capture electricty consumption of any live wire and store it in a database or view its live value through a flask webserver.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

#### Software Requirements
- Python 3.7
- Local MQTT Broker (Websockets Enabled)
- Flask
- MySQL DB
- MYSQL Python Connector
- Flask Table
- Python Date Time Lib

#### Hardware Requirements
- CT Sensor
- Node MCU(Esp8266)
- Laptop/ RPi
- WiFi enabled envioronment

### Installing

1. [Install python 3.7 (https://www.python.org/downloads/)]
2. [Install Mosquitto Broker (https://mosquitto.org/download/)]
3. Install Python packages through pip, run: pip install Flask Flask-Table 
4. [Install MySQL DB with python connector enabled (https://www.mysql.com/downloads/)]
5. Enter borker's IP address in MQTT.py
6. Enter correct DB details in both MQTT.py and app.py
7. Run MQTT.py and app.py

## Deployment

1. Make connections as shown in PCB design in "PCB Printing resources" or [follow (https://learn.openenergymonitor.org/electricity-monitoring/ctac/how-to-build-an-arduino-energy-monitor)]
2. Run mosquiito broker and MySQL DB.
3. Launch MQTT.py and app.py script
4. Open up local web browser to see login page
5. Default login username: admin, Password: admin

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* This projected was developed at National Council for Cement and Building Materials
* This project was completed under PS-1 of BITS Pilani




