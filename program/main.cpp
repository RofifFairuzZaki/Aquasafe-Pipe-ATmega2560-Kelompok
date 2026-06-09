#include <Arduino.h>

#include <avr/io.h>
#include <util/delay.h>

#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#include <stdio.h>
#include <stdlib.h>

LiquidCrystal_I2C lcd(0x27,16,2);

#define BUZZER PB4

// ================= USART =================

void USART_Init()
{
  uint16_t ubrr = 103;

  UBRR0H = (ubrr >> 8);
  UBRR0L = ubrr;

  UCSR0B = (1<<TXEN0);
  UCSR0C = (1<<UCSZ01) | (1<<UCSZ00);
}

void USART_SendChar(char c)
{
  while(!(UCSR0A & (1<<UDRE0)));
  UDR0 = c;
}

void USART_SendString(const char *s)
{
  while(*s)
  {
    USART_SendChar(*s++);
  }
}

// ================= ADC =================

void ADC_Init()
{
  ADMUX = (1<<REFS0);

  ADCSRA =
      (1<<ADEN)  |
      (1<<ADPS2) |
      (1<<ADPS1) |
      (1<<ADPS0);
}

uint16_t ADC_Read(uint8_t ch)
{
  ADMUX = (ADMUX & 0xF8) | ch;

  ADCSRA |= (1<<ADSC);

  while(ADCSRA & (1<<ADSC));

  return ADC;
}

float readAverage(uint8_t pin)
{
  long total = 0;

  for(uint8_t i=0;i<10;i++)
  {
    total += ADC_Read(pin);
    _delay_ms(5);
  }

  return (float)total/10.0;
}

// ================= Buzzer =================

void buzzerOn()
{
  tone(10,1000);
}

void buzzerOff()
{
  noTone(10);
}

// ================= Main =================

void setup()
{
  USART_Init();
  ADC_Init();

  pinMode(10,OUTPUT);

  lcd.init();
  lcd.backlight();

  lcd.setCursor(0,0);
  lcd.print(" AquaSafe Pipe ");
  lcd.setCursor(0,1);
  lcd.print(" System Ready ");

  delay(2000);
  lcd.clear();
}

void loop()
{
  float adcPH   = readAverage(0);
  float adcTDS  = readAverage(1);
  float adcTurb = readAverage(2);

  float ph   = adcPH * 14.0 / 1023.0;
  float tds  = adcTDS * 2000.0 / 1023.0;
  float turb = adcTurb * 2000.0 / 1023.0;

  const char *status;

  if((ph < 6.5) || (ph > 8.5) || (tds > 1200) || (turb > 1000))
  {
      status = "BAHAYA";
      buzzerOn();
  }
  else if((tds > 500) || (turb > 300))
  {
      status = "LUMAYAN";
      buzzerOff();
  }
  else
  {
      status = "AMAN";
      buzzerOff();
  }

  char buffer[50];

  dtostrf(ph,3,1,buffer);
  USART_SendString(buffer);

  USART_SendString(",");

  sprintf(buffer,"%d",(int)tds);
  USART_SendString(buffer);

  USART_SendString(",");

  sprintf(buffer,"%d",(int)turb);
  USART_SendString(buffer);

  USART_SendString(",");

  USART_SendString(status);
  USART_SendString("\r\n");

  lcd.setCursor(0,0);
  lcd.print("pH:");
  lcd.print(ph,1);
  lcd.print(" T:");
  lcd.print((int)tds);
  lcd.print("   ");

  lcd.setCursor(0,1);
  lcd.print("N:");
  lcd.print((int)turb);
  lcd.print(" ");
  lcd.print(status);
  lcd.print("      ");

  delay(1000);
}
