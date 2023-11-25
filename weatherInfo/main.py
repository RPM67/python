import requests
import json
import time
from roboSpeaker import commandSpeaker

print("Welcome to Weather News report by RPM".upper())
commandSpeaker("Welcome to Weather News report by RPM")


def city_weather_report():
    global weather_dict
    commandSpeaker("Enter the city name to get Weather report of : ")
    city = input("Enter the city name to get Weather report of (or 'exit' to quit) : ").lower()
    if city == 'exit':
        commandSpeaker("i hope you liked our service, please visit again")
        print("thank you for using our service, please visit again")
        exit()
    try:
        api_key = 'f6bc9e34a8484327bbd151628232309'
        url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
        re = requests.get(url)
        re.raise_for_status()  # Raise an exception for HTTP errors
        weather_dict = json.loads(re.text)

    except requests.exceptions.RequestException as e:
        print("Error fetching weather data. Please try again.")
        commandSpeaker("Error fetching weather data. Please check your internet connection and try again.")
        exit()
    except json.JSONDecodeError:
        print("Error fetching weather data. Please try again.")
        commandSpeaker("Error fetching weather data. Please check your internet connection and try again.")
        exit()
    print(f"the current temperature in {city} is {weather_dict['current']['temp_c']} degree celcius")
    commandSpeaker(f"the current temperature in {city} is {weather_dict['current']['temp_c']} degree celcius")

    # print(weather_dict)
    # print(weather_dict['location'].keys())
    commandSpeaker(f"Enter yes to see the complete weather report of {city}")
    print(f"Enter yes below to see the complete weather report of {city}")
    try:
        if userInput := input("Enter here : ").lower() == 'yes':
            commandSpeaker("the complete weather report is given below : ")
            keys_to_remove = [i for i in weather_dict['location'].keys() if
                              i == 'lat' or i == 'lon' or i == 'localtime_epoch']
            for i in keys_to_remove:
                weather_dict['location'].pop(i)
            print("\nCITY DETAILS :- ")
            for i, j in weather_dict['location'].items():
                print(f"{i.capitalize()} : {j}")

            # print(weather_dict)
            # print(weather_dict['current'].keys())

            keys_to_remove = [i for i in weather_dict['current'].keys() if
                              i != 'temp_c' and i != 'temp_f' and i != 'condition' and i != 'wind_dir' and i != 'wind_kph' and i != 'humidity' and i != 'feelslike_c' and i != 'last_updated']

            for i in keys_to_remove:
                weather_dict['current'].pop(i)

            print("\nCITY WEATHER DETAILS :- ")
            for i, j in weather_dict['current'].items():
                if i != 'condition':
                    print(f"{i.capitalize()} : {j}")
                else:
                    print(f"{i.capitalize()} : {j['text']}")
            time.sleep(5)
            commandSpeaker("Enter yes to see weather report of other cities")
            print("\nEnter yes below to see weather report of other cities")
            search_again = input("Enter here : ")
            if search_again.lower() == 'yes':
                city_weather_report()
            else:
                commandSpeaker("i hope you liked our service, please visit again")
                print("thank you for using our service, please visit again")
        else:
            print("thank you for using our service, please visit again")
            commandSpeaker("thank you for using our service, please visit again")

    except:
        commandSpeaker("oops some error occurred, please try again")
        print("thank you for using our service, please visit again")


if __name__ == "__main__":
    city_weather_report()
