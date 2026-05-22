#include <Wire.h>
#include "Adafruit_SHT31.h"

Adafruit_SHT31 sht31 = Adafruit_SHT31();

void setup() {
  Serial.begin(115200);
  sht31.begin(0x44);
}

void loop() {
  float temp = sht31.readTemperature();
  float hum  = sht31.readHumidity();

  int temp_int = (int)temp;   // remove decimal
  int hum_int  = (int)hum;

  // 🔥 Send BOTH values
  Serial.print(temp_int);
  Serial.print(",");          // separator
  Serial.println(hum_int);    // newline at end

  delay(1000);
}