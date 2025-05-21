const int fireSensorPin = 7;
void setup() {
 Serial.begin(9600);
 pinMode(fireSensorPin, INPUT);
}

void loop() {
  int fireDetected = digitalRead(fireSensorPin);
  Serial.println(fireDetected);
  // Se fogo for detectado, alarme automático entra em ação
  if (fireDetected == HIGH) {
  for (int i = 0; i < 8; i++) {
  delay(60);
  }
  return; // Sai do loop, ignora botão enquanto há fogo
}
  Serial.print("Fogo: ");
  Serial.print(fireDetected);

 delay(900); // Estabilização
}
