#define LED_BUILTIN 2
void setup() {
  serial.begin(9600);//print to monitor becuase set begin

  pinmode(LED_BUILTIN, OUTPUT);
}

void loop() {

  digitalwrile(LED_BUILTIN, 1);
  serial.print("สวัสดี ธีรวัฒน์ จำปาสัก");
  serial.print("light ...\n");
  delay(1000);

  digitalwrile(LED_BUILTIN, 0);
  serial.print("สวัสดี ธีรวัฒน์ จำปาสัก");
  serial.print("not light ...\n");
  delay(1000);
}
