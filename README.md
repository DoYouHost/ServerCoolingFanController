# Server Cooling Fan Controller

ESPHome-based server cooling fan controller using WT32-ETH01 (ESP32 with Ethernet).

## Features

- **Dual PWM outputs** for fan control
- **Temperature monitoring** with DS18B20 sensors
- **RPM monitoring** with pulse meters for all 4 fans
- **OLED display** (SSD1306 128x64) with status and error pages
- **Error detection** with automatic error page switching
- **Manual override** button for full speed operation
- **Runtime tracking** with persistent storage and reset button
- **Ethernet connectivity** for reliable network connection

## Hardware

- WT32-ETH01 development board
- 2N2222 NPN transistors for PWM control
- DS18B20 temperature sensors
- SSD1306 128x64 OLED display

## Files

- `serverCoolingFanController.yaml` - Main ESPHome configuration
- `docs/fan_pwm_2n2222.svg` - Hardware wiring schematic
- `docs/GPIO_PINOUT.txt` - GPIO pin assignments
