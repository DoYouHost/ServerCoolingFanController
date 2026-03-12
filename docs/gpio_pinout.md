# GPIO Pinout — LILYGO T-ETH-Lite ESP32-S3 (W5500)

## Board: T-ETH-LITE-ESP32S3
- MCU: ESP32-S3-WROOM-1
- Ethernet: W5500 (SPI)
- Flash: 16MB, PSRAM: 8MB

---

## Pins used internally by the board (NOT available)

| GPIO | Function          |
|------|-------------------|
| 5    | SD Card MISO      |
| 6    | SD Card MOSI      |
| 7    | SD Card SCLK      |
| 9    | W5500 CS          |
| 10   | W5500 SCK         |
| 11   | W5500 MISO        |
| 12   | W5500 MOSI        |
| 13   | W5500 INT         |
| 14   | W5500 RST         |
| 42   | SD Card CS        |

---

## Project pin assignments

### SPI Bus — ST7789V Display (Hardware SPI2)

| GPIO | Function       | Notes                          |
|------|----------------|--------------------------------|
| 15   | SPI2 CLK       | Display clock                  |
| 16   | SPI2 MOSI      | Display data                   |
| 47   | Display CS      | Chip select                    |
| 17   | Display DC      | Data/Command select            |
| 18   | Display RST     | Reset (active low)             |
| 8    | Display BL      | Backlight (PWM capable)        |

### Fan Control

| GPIO | Function       | Notes                          |
|------|----------------|--------------------------------|
| 21   | Fan PWM         | LEDC PWM output                |
| 38   | Fan 1 Tach      | Pulse counter input            |
| 39   | Fan 2 Tach      | Pulse counter input            |
| 40   | Fan 3 Tach      | Pulse counter input            |
| 41   | Fan 4 Tach      | Pulse counter input            |

### Sensors

| GPIO | Function       | Notes                          |
|------|----------------|--------------------------------|
| 4    | OneWire bus     | DS18B20 temperature sensors    |

### User Interface

| GPIO | Function       | Notes                          |
|------|----------------|--------------------------------|
| 3    | User button     | Input, internal pull-up        |
| 46   | Status LED      | ESPHome status blink           |
| 48   | Error LED       | Fan error strobe               |

### Reserved for future I2C

| GPIO | Function       | Notes                          |
|------|----------------|--------------------------------|
| 1    | I2C SDA         | Recommended by LILYGO examples |
| 2    | I2C SCL         | Recommended by LILYGO examples |

---

## Free / Unassigned GPIOs

| GPIO | Notes                              |
|------|------------------------------------|
| 0    | Boot button — use with caution     |

---

## Pin assignment rationale

- **SPI2 (GPIO15, 16):** ESP32-S3 has two user SPI peripherals (SPI2, SPI3).
  SPI3 is already used by W5500 on-board (GPIO9-14). SPI2 is free and
  GPIO15/16 are clean GPIOs with no boot restrictions.
- **Display DC/RST/BL (GPIO17, 18, 8):** Simple output pins, grouped near
  SPI2 pins for clean PCB routing. GPIO8 supports PWM for backlight dimming.
- **Fan PWM (GPIO21):** Clean output pin, no boot restrictions, PWM capable.
- **Fan SSR (GPIO45):** Controls solid state relay to cut fan power when off.
  Clean output pin, no boot restrictions.
- **Tach inputs (GPIO38-41):** Grouped consecutively for clean layout.
  All support pulse counter peripheral.
- **OneWire (GPIO4):** Same pin as current WT32-ETH01 design. No conflicts.
- **User button (GPIO3):** Clean input pin with internal pull-up available.
- **Status LED (GPIO46):** ESPHome status indicator (blink on warning/error).
- **Error LED (GPIO48):** Dedicated fan error strobe indicator.
- **I2C (GPIO1, 2):** Reserved but not used. These are the pins recommended
  by LILYGO's own I2C example (WireExample) for T-ETH-Lite-S3.

## Source

Pin definitions verified against:
- https://github.com/Xinyuan-LilyGO/LilyGO-T-ETH-Series/blob/master/examples/HelloServer/utilities.h
- https://github.com/Xinyuan-LilyGO/LilyGO-T-ETH-Series/blob/master/esphome/lilygo-eth-lite-esp32s3.yaml
