/*
A large part of this program (specifically the Arduino WiFi connection portion) is taken directly from Arduinos example file "WiFiWebServer" program.
The parts of the program modified for the power monitor project is sectioned off, the rest is taken directly from the example file.
Original program information:
 created 13 July 2010
 by dlf (Metodo2 srl)
 modified 31 May 2012
 by Tom Igoe

Senior Design Project Smart Home Appliance Power Monitor
Initially modified by Abe Wickstrom on 2/20/2020
Last Modified 3/23/2020 by Abe Wickstrom
 */

#include <SPI.h>
#include <WiFiNINA.h>

//Wifi information input 
char ssid[] = "Batcave1";        // your network SSID (name)
char pass[] = "PASSWORD";    // your network password

int status = WL_IDLE_STATUS;

WiFiServer server(80);

void setup() {
  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // check for the WiFi module:
  if (WiFi.status() == WL_NO_MODULE) {
    Serial.println("Communication with WiFi module failed!");
    // don't continue
    while (true);
  }

  String fv = WiFi.firmwareVersion();
  if (fv < WIFI_FIRMWARE_LATEST_VERSION) {
    Serial.println("Please upgrade the firmware");
  }

  // attempt to connect to Wifi network:
  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(ssid);
    // Connect to WPA/WPA2 network. Change this line if using open or WEP network:
    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:
    delay(10000);
  }
  server.begin();
  // you're connected now, so print out the status:
  printWifiStatus();
}


void loop() {
  // listen for incoming clients
  WiFiClient client = server.available();
  if (client) {
    Serial.println("new client");
    // an http request ends with a blank line
    boolean currentLineIsBlank = true;
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        Serial.write(c);
        // if you've gotten to the end of the line (received a newline
        // character) and the line is blank, the http request has ended,
        // so you can send a reply
        if (c == '\n' && currentLineIsBlank) {
          // send a standard http response header
          client.println("HTTP/1.1 200 OK");
          client.println("Content-Type: text/html");
          client.println("Connection: close");  // the connection will be closed after completion of the response
          client.println("Refresh: 120");  // refresh the page automatically every 120 sec
          client.println();
          client.println("<!DOCTYPE HTML>");
          client.println("<html>");
          
        //************************************************************************
        //Power monitor code modification starts here:
        //************************************************************************
        float sensorReadingAvg = 0;
        int sensorReadingSum = 0;
        //Take 100 readings from the analog input pins, and compute the Average reading
        for (int test = 1; test < 21; test++) { 
          int analogChannel = 0;
          int sensorReading = analogRead(analogChannel);
          sensorReadingSum = sensorReadingSum + sensorReading;
          sensorReadingAvg = sensorReadingSum/test;
          float voltage = sensorReading*(3.3/1023);
          float current = voltage / 6200; // For testing purposes, a 6200 Ohm resistor is being used
          client.print("Channel Num: ");
          client.print(analogChannel);
          client.print(", Voltage: ");
          client.print(voltage,3);
          client.print(" V, Current: ");
          client.print(current*1000,3);
          client.print(" mA ");
          client.println("<br />");
        }
          float voltAvg = sensorReadingAvg*(3.3/1023);
          float currentAvg = (voltAvg/6200)*1000;
          
          client.print("Voltage Average: ");
          client.print(voltAvg,3); 
          client.print("V, Current Average: ");
          client.print(currentAvg,3); //same current calculation as above
          client.print(" mA ");
          client.println("<br />");
          client.println("</html>");
          break;
        }
        //************************************************************************
        //power monitor code modification end here
        //************************************************************************
        if (c == '\n') {
          // you're starting a new line
          currentLineIsBlank = true;
        } else if (c != '\r') {
          // you've gotten a character on the current line
          currentLineIsBlank = false;
        }
      }
    }
    // give the web browser time to receive the data
    delay(1);

    // close the connection:
    client.stop();
    Serial.println("client disconnected");
  }
}


void printWifiStatus() {
  // print the SSID of the network you're attached to:
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // print your board's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  // print the received signal strength:
  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI):");
  Serial.print(rssi);
  Serial.println(" dBm");
}
