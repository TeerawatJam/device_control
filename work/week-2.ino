#define LED_BUILTIN 2
void setup() {
  Serial.begin(9600);//print to monitor becuase set begin
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  Serial.print("สวัสดี ธีรวัฒน์ จำปาสัก\n");

  digitalWrile(LED_BUILTIN, 1);
  Serial.print("light ...\n");
  delay(1000);

  digitalWrile(LED_BUILTIN, 0);
  Serial.print("not light ...\n");
  delay(1000);
}
