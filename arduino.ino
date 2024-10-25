// Código Arduino: Ligar ou desligar o LED com base nos comandos recebidos via serial

int ledPin12 = 12;  // Pino do LED12
int ledPin13 = 13;  // Pino do LED13

void setup() {
  pinMode(ledPin12, OUTPUT);  // Define o pino 13 como saída
    pinMode(ledPin13, OUTPUT);  // Define o pino 13 como saída

  Serial.begin(9600);  // Inicia a comunicação serial a 9600 baud
}

void loop() {
  // Verifica se há dados disponíveis na porta serial
  if (Serial.available() > 0) {
    char comando = Serial.read();  // Lê o comadsadndo enviado pelo Python

    if (comando == '1') {  // Se o comando for '1', liga o LED
      digitalWrite(ledPin13, HIGH);
      digitalWrite(ledPin12, LOW);
    }
    else if (comando == '0') {  // Se o comando for '0', desliga o LED
      digitalWrite(ledPin, HIGH);
      digitalWrite(ledPin13, LOW);
    }
  }
}