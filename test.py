from unittest import TestCase

from weather import Weather

# http://codekata.com/kata/kata04-data-munging/
class Measurement(object):
    def __init__(self, day, min, max):
        self.day = day
        self.min = min
        self.max = max

    def delta(self):
        return self.max - self.min


class MainTest(TestCase):
    def smoke_test(self):
        lines = [
            "   1  88    59    74          53.8       0.00 F       280  9.6 270  17  1.6  93 23 1004.5",
            "   2  79    63    71          46.5       0.00         330  8.7 340  23  3.3  70 28 1004.5"
        ]

        weather = Weather(lines)

    def load_test_data(self):
        data = open("weather.dat")
        lines = []
        for line in data:
            lines.append(line)
        return lines

    def test_file_all_lines_loaded(self):
        lines = self.load_test_data()
        self.assertEquals(len(lines), 33)

    def test_can_normalize_data(self):
        lines = self.load_test_data()
        normal = self.normalize(lines)
        first_measurement = normal[0]
        last_measurement = normal[-1]
        self.assertEquals(1, first_measurement.day)
        self.assertEquals(59, first_measurement.min)
        self.assertEquals(88, first_measurement.max)
        self.assertEquals(29, first_measurement.delta())

        self.assertEquals(30, last_measurement.day)
        self.assertEquals(45, last_measurement.min)
        self.assertEquals(90, last_measurement.max)
        self.assertEquals(45, last_measurement.delta())

    def test_find_lowest_delta_day(self):
        lines = self.load_test_data()
        normal = self.normalize(lines)

        result = sorted(normal, key=lambda measurement: measurement.delta())
        self.assertEquals(14, result[0].day)

    def normalize(self, data):
        measurements = []
        for row in data[2:-1]:
            line = row.split()
            day = int(line[0])
            min = int(line[2].replace("*", ""))
            max = int(line[1].replace("*", ""))
            measurements.append(Measurement(day, min, max))
        return measurements
