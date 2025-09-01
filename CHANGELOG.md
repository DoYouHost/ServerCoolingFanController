# 2025.3
## .2
- Changed logging level for pulse_counter component to INFO
- Added text_sensor for fan curves status
- Increased update interval for fan curves status to 60s
- Fixed JSON file parsing for fan curves
- Added fan curves JSON download after status is changed to "connected"
- Added AUTO mode for fan control
- Improved fan control logic for AUTO mode
- Changed default fan curve points
## .1
- Fixes for http_request handling JSON responses
## .0
- Added support for setting after how many seconds the fan error state is triggered
- When ESP is restarted fan states are restored with safe start sequence
- Testing support for fan curves via JSON configuration
# 2025.2
## .15
- Improved fan speed control logic
## .14
- Added support for showing 0% PWM if fan is off
## .13
- Improved error message display for fan status
- Added support for displaying fan error messages in a more user-friendly format
- Additional filtering for fan RPM sensors
- Manual override button now saves and restores fan states
## .12
- Changed update interval for RPM sensors
- Added throttle_average for RPM
- Changed display layout for better readability
## .11
- Added cabinet_fan_safe_start script
- Changed pulse_meter to pulse_counter
## .10
- Changed min_power to 0.7 for cabinet fan
- Changed display layout for better readability
- Added force_update: true
## .9
- Changed font to "Source Code Pro" for better readability
- Added %PWM on fan speed display
- Reduced throttle average to 2s
- Reduced timeout to 5s
## .8
- Changed font to "Roboto Mono" for better readability
- Increased font sizes for better readability
## .7
- Increased font sizes for better readability
- Modified pinout for fan tachometers
## .6
- Added clamp filters to fan speed sensors (fixes issue with RPM going crazy after fan is turned off and is spinning down)
## .5
- Invert ERROR_LED logic
## .4
- Fan pwm frequency changed to 19531 Hz
- Manual override button fan speed increased to 10
## .3
- Fan pwm frequency changed to 9765 Hz
## .2
- Fixed I2C pin assignments
## .1
- PCF8574 for more GPIOs
- Power supply for Rack Fans
- Increased fan step control from 4 to 10
- Added status_led
- Added error_led
## .0
- Testing if summary for update card in HA can be generated from CHANGELOG.md
- **Check for update** button moved to config section
- **Check for update** button new icon added
# 2025.1
## .1
- Testing prod / beta staging
## .0
- Initial release
