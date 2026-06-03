import requests

class WeatherAPI:
    def get_weather(self, city):
        url = f"https://wttr.in/{city}?format=j1"
        try:
            response = requests.get(url)

            if response.status_code == 404:
                print("City not found")
                return

            response.raise_for_status()
            data = response.json()

            temperature = data["current_condition"][0]["temp_C"]
            condition = data["current_condition"][0]["weatherDesc"][0]["value"]

            print(f"City: {city}")
            print(f"Temperature: {temperature}°C")
            print(f"Condition: {condition}")

        except requests.exceptions.RequestException:
            print("Network error occurred")
        except KeyError:
            print("Invalid data received")

def main():
    weather = WeatherAPI()
    weather.get_weather("Chennai")

if __name__ == "__main__":
    main()
