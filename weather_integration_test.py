import unittest
from tools import get_weather


class WeatherIntegrationTest(unittest.TestCase):
    def test_get_weather_for_existing_city(self):
        result = get_weather("London")

        self.assertIn("London", result)

        self.assertIn("City:", result)
        self.assertIn("Temperature:", result)
        self.assertIn("Condition:", result)
        self.assertIn("Humidity:", result)
        self.assertIn("Wind speed:", result)

    def test_get_weather_for_non_existing_city(self):
        result = get_weather("NoSuchCity_1234567890")

        self.assertIn("Could not get weather in NoSuchCity_1234567890", result)
        self.assertIn("NoSuchCity_1234567890", result)


if __name__ == "__main__":
    unittest.main()