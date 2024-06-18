import requests
from typing import Optional

def get_weather(api_key: str, city: str) -> None:

    if not api_key:
        raise ValueError("API key must be provided")
    if not city:
        raise ValueError("City must be provided")

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",

    }

    try:
        response = requests.get(base_url, params=params)
        data = response. json()

        if response.status_code == 200:
            # Extract relevant information from the API response
            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            temp_min = data["main"]["temp_min"]
            temp_max = data["main"]["temp_max"]
            pressure = data["main"] ["pressure"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]
            wind_speed = data["wind"] ["speed"]
            clouds = data["clouds"]["all"]
            visibility = data["visibility"]
            dew_point: Optional[float] = data.get("main", {}) .get("dew_point")
            rain: Optional[float] = data.get("rain", {}) .get("1h")

            print(f"WEATHER in {city}:")

            print(f"\t TEMERATURE: {temperature}℃")

            print(f"\tFeels Like: {feels_like}°C")
            print(f"\tMinimum TEMPERATURE: {temp_min}℃")

            print(f"\tMaximum TEMPERATURE: {temp_max}°℃")

            print(f"\tHumdity: {humidity}%")

            print(f"\tWind Speed: {wind_speed} m/s")

            print(f"\tCloud Coverage: {clouds}%")

            print(f"\tVisibility: {visibility} m")

            print(f"\tDew Point: {dew_point}°c")

            print(f"\tPressure: {pressure} hPa")

            print(f"\tRain: {rain} mm")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main() -> None:
    api_key = "6ac51341fbe25af0043f9a7e166961c4"
    city = input("Enter the name of city or PIN code: ")

    get_weather(api_key, city)

if _name=="main_":
    main()