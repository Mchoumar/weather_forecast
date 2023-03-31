import requests
from os import getenv


def get_data(city_name, forecast_days=None, data_view=None):
    # requesting api from openweather and extracting it
    api_key = getenv("API_weather")
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    # filters the data to represent only the ones related to the forecast
    filtered_data = data["list"]

    # filtering the data depending on the number of days
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]

    return filtered_data


if __name__ == "__main__":
    print(get_data(city_name='tokyo'))