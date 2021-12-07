import pprint
import requests

API_KEY_YANDEX_WEATHER = 'e7a7e260-ff96-444a-bf2c-15a7d6b70521'
FIELDS = ["temp_max", "temp_min"]


class YandexWeatherForecast:
 
    URL = 'https://api.weather.yandex.ru/v1/forecast?'
    
    def __init__(self, key):
        self.key = key
        self.headers = {'X-Yandex-API-Key': key}
        
    def get_weather_week_forecast(self, city, fields):
        
        data = requests.get(f'{self.URL}{city}', headers=self.headers).json()
        week_forecast = []
        
        for forecast in data['forecasts']:
            data = {'date': forecast["date"]}
            print(f'data: {data}')
            for field in fields:
                value = forecast["parts"]["day"].get(field, None)
                if value is not None:
                    data[field] = value
            week_forecast.append(data)
        
        return week_forecast


class CityInfo:
    
    def __init__(self, city, forecast_provider):
        self.city = city.lower()
        self._forecast_provider = forecast_provider
        
    def weather_forecast(self, fields):
        return self._forecast_provider.get_weather_week_forecast(self.city, fields)     


def _main():
    weather_api = YandexWeatherForecast(API_KEY_YANDEX_WEATHER)
    city_name = ""
    city = CityInfo(city_name, weather_api)
    pprint.pprint(city.weather_forecast(FIELDS))


if __name__ == "__main__":
    _main()
        