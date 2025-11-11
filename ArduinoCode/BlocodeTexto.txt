#define MAXIMWIRE_EXTERNAL_PULLUP
#include <U8g2lib.h>
#include <SPI.h>
#include <SD.h>
#include <TinyGPSPlus.h>
#include <MaximWire.h>

// Inicializa o display com SPI
U8G2_SH1106_128X64_NONAME_F_4W_HW_SPI u8g2(U8G2_R0, /* cs=*/ 10, /* dc=*/ 8, /* reset=*/ 9);

// Pinos do barramento 1-Wire
#define PIN_BUS 6

// Pino CS do módulo SD
#define PIN_SD_CS 4

MaximWire::Bus bus(PIN_BUS);

// Endereços dos sensores
MaximWire::Address address1, address2, address3;

TinyGPSPlus gps;
File arquivo;

// Controle de tempo para GPS
unsigned long lastTime = 0;
const unsigned long intervalo = 3000; // 3 segundos

void inicializarSD() {
    if (!SD.begin(PIN_SD_CS)) {
        u8g2.clearBuffer();
        u8g2.setFont(u8g2_font_ncenB08_tr);
        u8g2.drawStr(0, 24, "Erro no SD!");
        u8g2.sendBuffer();
        while (true); // Para execução se o SD falhar
    }

    const char *arquivos[] = {"gps_data.txt", "Sensor1.txt", "Sensor2.txt", "Sensor3.txt"};
    for (int i = 0; i < 4; i++) {
        File arquivo = SD.open(arquivos[i], FILE_WRITE);
        if (arquivo) {
            if (i == 0) {
                arquivo.println("Latitude,Longitude,Altitude,Satelites");
            }
            arquivo.close();
        }
    }
}

void setup() {
    Serial.begin(9600);
    Serial1.begin(9600);
    u8g2.begin();

    Serial.println("Iniciando detecção de sensores...");

    inicializarSD();

    // Descobrir dispositivos no barramento
    MaximWire::Discovery discovery = bus.Discover();
    int sensorIndex = 0;

    while (discovery.HaveMore()) {
        MaximWire::Address address;
        if (discovery.FindNextDevice(address) && address.GetModelCode() == MaximWire::DS18B20::MODEL_CODE) {
            switch (sensorIndex) {
                case 0:
                    address1 = address;
                    Serial.print("Sensor 1 encontrado: ");
                    Serial.println(address.ToString());
                    break;
                case 1:
                    address2 = address;
                    Serial.print("Sensor 2 encontrado: ");
                    Serial.println(address.ToString());
                    break;
                case 2:
                    address3 = address;
                    Serial.print("Sensor 3 encontrado: ");
                    Serial.println(address.ToString());
                    break;
                default:
                    Serial.println("Mais de 3 sensores encontrados. Ignorando os demais.");
                    break;
            }
            sensorIndex++;
        }
    }

    if (sensorIndex < 3) {
        Serial.println("Atenção: nem todos os sensores foram detectados!");
    }
}

float lerTemperatura(const MaximWire::Address &address) {
    MaximWire::DS18B20 sensor(address);
    sensor.Update(bus); // Atualiza os dados do sensor
    return sensor.GetTemperature<float>(bus); // Obtém a temperatura
}

void salvarTemperatura(const char *nomeArquivo, float temperatura) {
    if (temperatura == -127.0 || temperatura == 85.0) return; // Validações iniciais

    File arquivoSensor = SD.open(nomeArquivo, FILE_WRITE);
    if (!arquivoSensor) {
        Serial.print("Erro ao gravar no arquivo ");
        Serial.println(nomeArquivo);
        return;
    }
    arquivoSensor.print("Temperatura: ");
    arquivoSensor.print(temperatura, 2);
    arquivoSensor.println(" C");
    arquivoSensor.close();
}

void gravarDadosGPS(double latitude, double longitude, double altitude, int satelites) {
    File arquivo = SD.open("gps_data.txt", FILE_WRITE);
    if (!arquivo) {
        Serial.println("Erro ao gravar no arquivo 'gps_data.txt'.");
        return;
    }
    arquivo.print(latitude, 6);
    arquivo.print(",");
    arquivo.print(longitude, 6);
    arquivo.print(",");
    arquivo.print(altitude, 2);
    arquivo.print(",");
    arquivo.println(satelites);
    arquivo.close();
}

void exibirDadosGPS(double latitude, double longitude, double altitude, int satelites) {
    u8g2.clearBuffer();
    u8g2.setFont(u8g2_font_ncenB08_tr);

    char buffer[32];

    snprintf(buffer, sizeof(buffer), "Lat: %.6f", latitude);
    u8g2.drawStr(0, 12, buffer);

    snprintf(buffer, sizeof(buffer), "Lon: %.6f", longitude);
    u8g2.drawStr(0, 24, buffer);

    snprintf(buffer, sizeof(buffer), "Alt: %.2f m", altitude);
    u8g2.drawStr(0, 36, buffer);

    snprintf(buffer, sizeof(buffer), "Sat: %d", satelites);
    u8g2.drawStr(0, 48, buffer);

    u8g2.sendBuffer();
}

void verificarSensores() {
    u8g2.clearBuffer();
    u8g2.setFont(u8g2_font_ncenB08_tr);

    if (address1.IsValid()) {
        u8g2.drawStr(0, 12, "Sensor 1: OK");
        Serial.println("Sensor 1: OK");
    } else {
        u8g2.drawStr(0, 12, "Sensor 1: OFF");
        Serial.println("Sensor 1: OFF");
    }
    u8g2.sendBuffer();
    delay(1000);

    if (address2.IsValid()) {
        u8g2.clearBuffer();
        u8g2.drawStr(0, 24, "Sensor 2: OK");
        Serial.println("Sensor 2: OK");
    } else {
        u8g2.clearBuffer();
        u8g2.drawStr(0, 24, "Sensor 2: OFF");
        Serial.println("Sensor 2: OFF");
    }
    u8g2.sendBuffer();
    delay(1000);

    if (address3.IsValid()) {
        u8g2.clearBuffer();
        u8g2.drawStr(0, 36, "Sensor 3: OK");
        Serial.println("Sensor 3: OK");
    } else {
        u8g2.clearBuffer();
        u8g2.drawStr(0, 36, "Sensor 3: OFF");
        Serial.println("Sensor 3: OFF");
    }
    u8g2.sendBuffer();
    delay(1000);
}

void loop() {
    verificarSensores();

    while (Serial1.available() > 0) {
        if (gps.encode(Serial1.read()) && gps.location.isUpdated()) {
            unsigned long currentMillis = millis();

            if (currentMillis - lastTime < intervalo) return; // Early return para respeitar o intervalo
            lastTime = currentMillis;

            double latitude = gps.location.lat();
            double longitude = gps.location.lng();
            double altitude = gps.altitude.meters();
            int satelites = gps.satellites.value();

            // Grava os dados no cartão SD
            gravarDadosGPS(latitude, longitude, altitude, satelites);

            // Exibe as informações de GPS no LCD
            exibirDadosGPS(latitude, longitude, altitude, satelites);

            // Leitura e gravação das temperaturas dos sensores
            if (address1.IsValid()) {
                float temp1 = lerTemperatura(address1);
                salvarTemperatura("Sensor1.txt", temp1);
                Serial.print("Temperatura Sensor 1: ");
                Serial.println(temp1);
            }
            if (address2.IsValid()) {
                float temp2 = lerTemperatura(address2);
                salvarTemperatura("Sensor2.txt", temp2);
                Serial.print("Temperatura Sensor 2: ");
                Serial.println(temp2);
            }
            if (address3.IsValid()) {
                float temp3 = lerTemperatura(address3);
                salvarTemperatura("Sensor3.txt", temp3);
                Serial.print("Temperatura Sensor 3: ");
                Serial.println(temp3);
            }
        }
    }
}