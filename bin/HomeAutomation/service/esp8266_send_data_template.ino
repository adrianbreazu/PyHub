// include section
#include <SoftwareSerial.h>
#include "DHT.h"

// ESP8266 section
#define SSID "__SSID__"
#define PASS "__PASS__"
#define DEBUG true
#define IP "__IP__" // pihub ip address
#define PORT "__PORT__" //pihub port
#define SENSOR_ID "__SENSOR_ID__"
String POST = "POST /ambient/sensor_data HTTP/1.1";

// DHT11 section
#define DHTPIN 4
#define DHTTYPE DHT22   // DHT 22
DHT dht(DHTPIN, DHTTYPE);

//init esp8266
SoftwareSerial esp8266(2,3);

//bmp180
Adafruit_BMP085 bmp;

void setup()
{
  boolean connectionEstablished = false;
  Serial.begin(9600);

  esp8266.begin(9600);
  dht.begin();

  if (!bmp.begin()) {
    Serial.println("No BMP sensor!");
  }

  delay(2000);

  sendData("AT+RST", 2000, DEBUG);
  delay(2000);

  sendData("AT", 2000, DEBUG);
  delay(2000);

  initialize();
  while (!connectionEstablished) {
    connectionEstablished = connectToNetwork();
  }
    delay(2000);
}

void loop(){
  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  char buffer[10];
  String temperature = dtostrf(t, 4, 1, buffer);
  String humidity = dtostrf(h, 4, 1, buffer);

  Serial.print("Temperature = ");
  Serial.println(temperature);

  Serial.print("Humidity = ");
  Serial.println(humidity);

  Serial.print("Pressure = ");
  Serial.print(bmp.readPressure());
  float p = bmp.readPressure();
  String pressure = dtostrf(p, 6, 1, buffer);

  if (sendAmbiendData(temperature, humidity, pressure)) {
    delay(60000);
  }
}

boolean initialize() {
  sendData("AT+CWMODE=1", 2000, DEBUG);
  delay(2000);
  sendData("AT+CIPMODE=0", 2000, DEBUG);
  delay(2000);
  sendData("AT+CIPMUX=1", 2000, DEBUG);
  delay(2000);
}

boolean sendAmbiendData(String temperature, String humidity, String pressure){
  String response = "";

  // send Start command
  String cmd = "AT+CIPSTART=0,\"TCP\",\"";
  cmd += IP;
  cmd += "\",";
  cmd += PORT;
  response = sendData(cmd, 2000, DEBUG);
  delay(2000);

  if(response.indexOf("ERROR") > 0){
    return false;
  }

  String json_message = "";
  json_message = "{ \"sensor_id\": \"";
  json_message += SENSOR_ID;
  json_message +=  "\", \"temperature\": \"";
  json_message += temperature;
  json_message += "\", \"humidity\": \"";
  json_message += humidity;
  json_message += "\", \"pressure\": \"";
  json_message += pressure;
  json_message += "\" }";

 Serial.println(json_message);

  cmd = "";
  cmd = POST;
  cmd += "\r\n";
  cmd += "Host: ";
  cmd += IP;
  cmd += "\r\n";
  cmd += "Content-Type: application/json";
  cmd += "\r\n";
  cmd += "Content-Length: ";
  cmd += json_message.length();
  cmd += "\r\n\r\n";
  cmd += json_message;

  String length_msg= "AT+CIPSEND=0,";
  length_msg += cmd.length();

  response = sendData(length_msg, 2000, DEBUG);
  if(response.indexOf(">") >= 0) {
    sendData(cmd, 2000, DEBUG);
  } else {
    sendData("AT+CIPCLOSE", 2000, DEBUG);
  }
}

boolean connectToNetwork(){
  String response ="";

  String cmd="AT+CWJAP=\"";
  cmd+=SSID;
  cmd+="\",\"";
  cmd+=PASS;
  cmd+="\"";
  response = sendData(cmd, 10000, DEBUG);

  delay(15000);

  if(response.indexOf("OK") > 0) {
    return true;
  }
  else {
    return false;
  }
}

String sendData(String command, const int timeout, boolean debug)
{
    String response = "";
    esp8266.println(command); // send the read character to the esp8266
    long int time = millis();

    while( (time+timeout) > millis()) {
      while(esp8266.available()) {
        // The esp has data so display its output to the serial window
        char c = esp8266.read(); // read the next character.
        response+=c;
      }
    }
    if(debug) {
      Serial.println(response);
    }
    return response;
}