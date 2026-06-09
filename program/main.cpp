#include <Arduino.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

#define PH_PIN    A0
#define TDS_PIN   A1
#define TURB_PIN  A2
#define BUZZER    10

float readAverage(uint8_t pin, uint8_t samples = 10);

void setup()
{
    Serial.begin(9600);

    pinMode(BUZZER, OUTPUT);
    digitalWrite(BUZZER, LOW);

    lcd.init();
    lcd.backlight();

    lcd.setCursor(0, 0);
    lcd.print(" AquaSafe Pipe ");
    lcd.setCursor(0, 1);
    lcd.print(" System Ready ");
    delay(2000);

    lcd.clear();
}

void loop()
{
    float adcPH   = readAverage(PH_PIN);
    float adcTDS  = readAverage(TDS_PIN);
    float adcTurb = readAverage(TURB_PIN);

    float ph   = adcPH * 14.0 / 1023.0;
    float tds  = adcTDS * 2000.0 / 1023.0;
    float turb = adcTurb * 2000.0 / 1023.0;

    const char *status;

    if ((ph < 6.5) || (ph > 8.5) || (tds > 1200) || (turb > 1000))
    {
        status = "BAHAYA";
        tone(BUZZER, 1000);
    }
    else if ((tds > 500) || (turb > 300))
    {
        status = "LUMAYAN";
        noTone(BUZZER);
    }
    else
    {
        status = "AMAN";
        noTone(BUZZER);
    }

    // FORMAT UNTUK PYTHON
    Serial.print(ph, 1);
    Serial.print(",");
    Serial.print((int)tds);
    Serial.print(",");
    Serial.print((int)turb);
    Serial.print(",");
    Serial.println(status);

    lcd.setCursor(0, 0);
    lcd.print("pH:");
    lcd.print(ph, 1);
    lcd.print(" T:");
    lcd.print((int)tds);
    lcd.print("   ");

    lcd.setCursor(0, 1);
    lcd.print("N:");
    lcd.print((int)turb);
    lcd.print(" ");
    lcd.print(status);
    lcd.print("      ");

    delay(1000);
}

float readAverage(uint8_t pin, uint8_t samples)
{
    long total = 0;

    for (uint8_t i = 0; i < samples; i++)
    {
        total += analogRead(pin);
        delay(5);
    }

    return (float)total / samples;
}
