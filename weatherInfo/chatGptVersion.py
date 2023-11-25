import requests
import json
import time


def get_weather(city):
    try:
        api_key = "f6bc9e34a8484327bbd151628232309"  # Replace with your actual API key
        url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        return None
    except json.JSONDecodeError:
        return None


def display_weather(weather_data):
    if weather_data is None:
        print("Error fetching weather data. Please try again.")
        return

    city = weather_data['location']['name']
    temperature_c = weather_data['current']['temp_c']

    print(f"The current temperature in {city} is {temperature_c}°C")


def main():
    print("Welcome to Weather News report by RPM".upper())

    while True:
        city = input("Enter the city name to get Weather report (or 'exit' to quit): ")
        if city.lower() == 'exit':
            print("Thank you for using our service. Goodbye!")
            break

        weather_data = get_weather(city)
        display_weather(weather_data)


if __name__ == "__main__":
    main()
