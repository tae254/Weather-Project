import requests

API_KEY = '0a2d7a179ff19902a1b014c6d82beff1'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'imperial',
    }
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=imperial"
    print(f"Requesting URL: {url}")
    response = requests.get(BASE_URL, params=params)
    print(response.json())
    return response.json()

def display_weather(weather_data):
    if weather_data['cod'] != 200:
        print(f"City not found: {weather_data['message']}")
        return

    city = weather_data['name']
    country = weather_data['sys']['country']
    temp = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    print(f"\nWeather in {city}, {country}:")
    print(f"Temperature: {temp}")
    print(f"Humidity: {humidity}")
    print(f"Wind speed: {wind_speed}")
    print(f"Description: {description}")

def main():
    print("Welcome to RJ's Weather App")
    while True:
        city_name = input("Enter city name: ")
        if city_name.lower() == 'exit':
            print("Thank you for using RJ's Weather App")
            break
        weather_data = get_weather(city_name)
        display_weather(weather_data)

if __name__ == '__main__':
    main()
