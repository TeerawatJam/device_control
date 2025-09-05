#include <ESP32Servo.h>

Servo myservo;
int angle;

void setup() {
  Serial.begin(9600);
  myservo.attach(22);
  Serial.println("Enter angle: 90, 180, 30, or 120");
}

void loop() {
  if (Serial.available() > 0) {
    angle = Serial.parseInt(); // อ่านเป็นจำนวนเต็ม
    if (angle == 90 || angle == 180 || angle == 30 || angle == 120) {
      Serial.print("Servo Motor => ");
      Serial.println(angle);
      myservo.write(angle);
    } else {
      Serial.println("Invalid angle! Use 90, 180, 30, or 120");
    }
    delay(1000);
  }
}