# Project 3: Weather CLI

## 🎯 Goal
Learn APIs by fetching weather data.

---

## 📌 Start Here

First install requests:
```bash
pip install requests
```

Then create this:

```python
# weather.py - Get weather for a city
import requests

API_KEY = "YOUR_API_KEY"  # Get free key from openweathermap.org

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    
    print(f"{city}: {temp}°C, {desc}")

city = input("Enter city: ")
get_weather(city)
```

Save as `project-3-weather/weather.py`

---

## 🚀 Next Steps

1. **Get API key**
   - Free from: https://openweathermap.org/api

2. **Add multiple cities**
   - Let users check weather for multiple cities

3. **Add forecasts**
   - Use 5-day forecast API

4. **Add location detection**
   - Use geolocation to get user's city

5. **Save favorites**
   - Remember frequently checked cities

---

## 💡 Tips

- Start with one city
- Handle API errors gracefully
- Try different weather APIs
- Display more weather info (humidity, wind, etc.)
