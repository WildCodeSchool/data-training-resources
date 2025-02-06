# SNCF Train Prices Scraper 🚅

## Description

This Python script automates the process of retrieving train ticket prices from SNCF Connect (sncf-connect.com). It uses Selenium WebDriver to simulate user interactions and extract pricing information for train journeys between specified French cities.

## Features

- Automated search for train tickets between any two French cities
- Extracts multiple journey options with detailed information:
  - Departure and arrival times
  - Station names
  - First and second class prices
- Uses real Chrome profile to avoid detection
- Implements human-like behavior with random delays and mouse movements
- Handles dynamic page loading and suggestions

## Prerequisites

- Python 3.x
- Google Chrome browser
- Chrome WebDriver
- A valid Chrome profile

## Required Libraries

```bash
pip install selenium
pip install webdriver-manager
```

## Configuration

Before running the script, you need to set up your Chrome profile path. By default, it's configured for Windows:

```python
options.add_argument(r"--user-data-dir=C:\Users\coach\AppData\Local\Google\Chrome\User Data")
options.add_argument(r"--profile-directory=Default")
```

Modify these paths according to your system configuration.

## Usage

1. Run the script:
```bash
python sncf_scraper.py
```

2. Enter the requested information when prompted:
- Departure city
- Arrival city

3. The script will:
- Open Chrome with your profile
- Navigate to SNCF Connect
- Input your travel details
- Extract and display available train options
- Show prices for both first and second class

## Output Example

```
Prix recommandé: 45€
-------------------
Départ: 10:30 de PARIS GARE DE LYON
Arrivée: 12:30 à LYON PART DIEU
1er Prix: 89€ / 2ème Prix: 45€
-------------------
```

## Important Notes

- The script uses your real Chrome profile to avoid CAPTCHA and authentication issues
- Random delays are implemented to simulate human behavior
- Keep the Chrome window visible during execution
- Do not interact with the browser while the script is running
- The script includes a 10-second delay at the end before closing

## Technical Details

The script utilizes several Selenium features:
- WebDriverWait for handling dynamic content
- ActionChains for simulating mouse movements
- JavaScript execution for smooth scrolling and input handling
- CSS and XPath selectors for element location

## Limitations

- Works only with SNCF Connect's current layout (as of 2025)
- Requires a stable internet connection
- May need adjustments if SNCF Connect updates their website structure

## Legal Notice

This script is for educational purposes only. Make sure to comply with SNCF Connect's terms of service when using automated tools.

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---
Made with ❤️ for Wild Code School Lille group working on train travel automation
