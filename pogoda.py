import requests
import bs4

response = requests.get("https://yandex.ru/pogoda")

if response.status_code == 200:
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    current_weather = soup.find(class_="temp__value").get_text()
    print(f"Текущая температура: {current_weather}°C")

    week_forecast = soup.find_all(class_="forecast-briefly__day")
    print("Погода на неделю:")

    for forecast in week_forecast:
        day = forecast.find(class_="forecast-briefly__name").get_text()
        weather = forecast.find(class_="forecast-briefly__condition").get_text()
        temperature = forecast.find(class_="forecast-briefly__temp .temp__value").get_text() + "°C"

        print(day + ":", weather + ",", temperature)
else:
    print("Не удалось получить информацию о погоде.")

