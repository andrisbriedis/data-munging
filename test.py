from unittest import TestCase

from file_loader import load_test_data
from normalizer import normalize_football, normalize


# http://codekata.com/kata/kata04-data-munging/
class MainTest(TestCase):

    def test_football_file_all_lines_loaded(self):
        lines = load_test_data('football.dat')
        self.assertEqual(len(lines), 22)

    def test_file_all_lines_loaded(self):
        lines = load_test_data('weather.dat')
        self.assertEqual(len(lines), 33)

    def test_can_normalize_data(self):
        lines = load_test_data('weather.dat')
        normal = normalize(lines)
        first_measurement = normal[0]
        last_measurement = normal[-1]
        self.assertEqual(1, first_measurement.day)
        self.assertEqual(59, first_measurement.min)
        self.assertEqual(88, first_measurement.max)
        self.assertEqual(29, first_measurement.delta())

        self.assertEqual(30, last_measurement.day)
        self.assertEqual(45, last_measurement.min)
        self.assertEqual(90, last_measurement.max)
        self.assertEqual(45, last_measurement.delta())

    def test_find_lowest_delta_day(self):
        lines = load_test_data('weather.dat')
        normal = normalize(lines)

        result = self.find_lowest(normal)
        self.assertEqual(14, result.day)

    def find_lowest(self, normal):
        return sorted(normal, key=lambda measurement: measurement.delta())[0]

    def test_can_normalize_football_data(self):
        lines = load_test_data('football.dat')
        normal = normalize_football(lines)
        first_measurement = normal[0]
        last_measurement = normal[-1]
        self.assertEqual('Arsenal', first_measurement.name)
        self.assertEqual(79, first_measurement.forward)
        self.assertEqual(36, first_measurement.against)
        self.assertEqual(43, first_measurement.delta())

        self.assertEqual('Leicester', last_measurement.name)
        self.assertEqual(30, last_measurement.forward)
        self.assertEqual(64, last_measurement.against)
        self.assertEqual(34, last_measurement.delta())

    def test_find_lowest_delta_team(self):
        lines = load_test_data('football.dat')
        normal = normalize_football(lines)

        result = self.find_lowest(normal)
        self.assertEqual("Aston_Villa", result.name)
