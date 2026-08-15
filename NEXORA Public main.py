import webbrowser
import requests

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen


APP_NAME = "NEXORA Public"


def open_maps(search):
    """Open a Google Maps search."""
    url = "https://www.google.com/maps/search/?api=1&query=" + requests.utils.quote(search)
    webbrowser.open(url)


class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(
            orientation="vertical",
            padding=12,
            spacing=10
        )

        title = Label(
            text="NEXORA Public",
            font_size="30sp",
            bold=True,
            size_hint_y=None,
            height=60
        )

        subtitle = Label(
            text="Explore places, transport and weather",
            font_size="16sp",
            size_hint_y=None,
            height=40
        )

        root.add_widget(title)
        root.add_widget(subtitle)

        scroll = ScrollView()

        grid = GridLayout(
            cols=2,
            spacing=10,
            padding=5,
            size_hint_y=None
        )

        grid.bind(minimum_height=grid.setter("height"))

        categories = [
            ("🚆 Railway Stations", "railway station"),
            ("✈ Airports", "airport"),
            ("🚌 Bus Stations", "bus station"),
            ("🚕 Taxis", "taxi"),
            ("🏛 Tourist Places", "tourist attractions"),
            ("🏥 Hospitals", "hospital"),
            ("🍴 Restaurants", "restaurants"),
            ("🏨 Hotels", "hotels"),
            ("🛍 Shopping", "shopping malls"),
            ("🏧 ATMs", "ATM"),
            ("⛽ Petrol Pumps", "petrol pump"),
            ("💊 Pharmacies", "pharmacy"),
            ("🏦 Banks", "bank"),
            ("🎓 Schools", "schools"),
            ("🏋 Gyms", "gyms"),
            ("🌳 Parks", "parks"),
            ("📍 Places", "places")
        ]

        for title_text, search_text in categories:

            button = Button(
                text=title_text,
                font_size="17sp",
                size_hint_y=None,
                height=65
            )

            button.bind(
                on_press=lambda instance, s=search_text:
                open_maps(s)
            )

            grid.add_widget(button)

        weather_button = Button(
            text="🌤 WEATHER",
            font_size="18sp",
            size_hint_y=None,
            height=65
        )

        weather_button.bind(
            on_press=self.open_weather
        )

        grid.add_widget(weather_button)

        scroll.add_widget(grid)
        root.add_widget(scroll)

        search_layout = BoxLayout(
            size_hint_y=None,
            height=55,
            spacing=5
        )

        self.search_box = TextInput(
            hint_text="Search any place...",
            multiline=False,
            font_size="17sp"
        )

        search_button = Button(
            text="SEARCH",
            size_hint_x=None,
            width=110
        )

        search_button.bind(
            on_press=self.search_place
        )

        search_layout.add_widget(self.search_box)
        search_layout.add_widget(search_button)

        root.add_widget(search_layout)

        self.add_widget(root)

    def search_place(self, instance):
        query = self.search_box.text.strip()

        if query:
            open_maps(query)

    def open_weather(self, instance):
        self.manager.current = "weather"


class WeatherScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        title = Label(
            text="🌤 WEATHER",
            font_size="30sp",
            bold=True,
            size_hint_y=None,
            height=60
        )

        self.city = TextInput(
            hint_text="Enter city name",
            multiline=False,
            font_size="18sp",
            size_hint_y=None,
            height=55
        )

        check = Button(
            text="CHECK WEATHER",
            font_size="18sp",
            size_hint_y=None,
            height=60
        )

        check.bind(
            on_press=self.get_weather
        )

        self.result = Label(
            text="Enter a city to check the weather.",
            font_size="18sp",
            halign="center"
        )

        back = Button(
            text="BACK",
            size_hint_y=None,
            height=55
        )

        back.bind(
            on_press=self.go_back
        )

        root.add_widget(title)
        root.add_widget(self.city)
        root.add_widget(check)
        root.add_widget(self.result)
        root.add_widget(back)

        self.add_widget(root)

    def get_weather(self, instance):

        city = self.city.text.strip()

        if not city:
            self.result.text = "Please enter a city."
            return

        self.result.text = "Loading weather..."

        try:

            geo_url = (
                "https://geocoding-api.open-meteo.com/v1/search"
                "?name="
                + requests.utils.quote(city)
                + "&count=1&language=en&format=json"
            )

            geo_response = requests.get(
                geo_url,
                timeout=10
            )

            geo_data = geo_response.json()

            if not geo_data.get("results"):
                self.result.text = "City not found."
                return

            location = geo_data["results"][0]

            latitude = location["latitude"]
            longitude = location["longitude"]
            name = location["name"]

            weather_url = (
                "https://api.open-meteo.com/v1/forecast"
                "?latitude=" + str(latitude)
                + "&longitude=" + str(longitude)
                + "&current=temperature_2m,relative_humidity_2m,"
                "apparent_temperature,wind_speed_10m"
            )

            weather_response = requests.get(
                weather_url,
                timeout=10
            )

            weather = weather_response.json()

            current = weather.get("current", {})

            temperature = current.get(
                "temperature_2m",
                "N/A"
            )

            humidity = current.get(
                "relative_humidity_2m",
                "N/A"
            )

            feels = current.get(
                "apparent_temperature",
                "N/A"
            )

            wind = current.get(
                "wind_speed_10m",
                "N/A"
            )

            self.result.text = (
                f"{name}\n\n"
                f"Temperature: {temperature} °C\n"
                f"Feels like: {feels} °C\n"
                f"Humidity: {humidity}%\n"
                f"Wind: {wind} km/h"
            )

        except Exception as error:

            self.result.text = (
                "Weather error.\n\n"
                + str(error)
            )

    def go_back(self, instance):
        self.manager.current = "home"


class NEXORAApp(App):

    def build(self):

        manager = ScreenManager()

        manager.add_widget(
            HomeScreen(name="home")
        )

        manager.add_widget(
            WeatherScreen(name="weather")
        )

        return manager


if __name__ == "__main__":
    NEXORAApp().run()
