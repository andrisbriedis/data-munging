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

class Score(object):
    def __init__(self, name, forward, against):
        self.name = name
        self.forward = forward
        self.against = against

    def delta(self):
        return abs(self.forward - self.against)

class MainTest(TestCase):
    def smoke_test(self):
        lines = [
            "   1  88    59    74          53.8       0.00 F       280  9.6 270  17  1.6  93 23 1004.5",
            "   2  79    63    71          46.5       0.00         330  8.7 340  23  3.3  70 28 1004.5"
        ]

        weather = Weather(lines)

    def load_test_data(self,filename):
        lines = []
        with open(filename) as data:
            for line in data:
                lines.append(line)

        return lines

    def test_football_file_all_lines_loaded(self):
        lines = self.load_test_data('football.dat')
        self.assertEqual(len(lines), 22)

    def test_file_all_lines_loaded(self):
        lines = self.load_test_data('weather.dat')
        self.assertEqual(len(lines), 33)

    def test_can_normalize_data(self):
        lines = self.load_test_data('weather.dat')
        normal = self.normalize(lines)
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
        lines = self.load_test_data('weather.dat')
        normal = self.normalize(lines)

        result = sorted(normal, key=lambda measurement: measurement.delta())
        self.assertEqual(14, result[0].day)


    def test_can_normalize_football_data(self):
        lines = self.load_test_data('football.dat')
        normal = self.normalize_football(lines)
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
        lines = self.load_test_data('football.dat')
        normal = self.normalize_football(lines)

        result = sorted(normal, key=lambda score: score.delta())
        self.assertEqual("Aston_Villa", result[0].name)

    def normalize_football(self, data):
        team_score = []
        for row in data[1:]:
            if row.strip().startswith('-----'):
                continue
            line = row.split()
            name = line[1]
            forward = int(line[6])
            against = int(line[8])
            team_score.append(Score(name, forward, against))
        return team_score

    def normalize(self, data):
        measurements = []
        for row in data[2:-1]:
            line = row.split()
            day = int(line[0])
            min = int(line[2].replace("*", ""))
            max = int(line[1].replace("*", ""))
            measurements.append(Measurement(day, min, max))
        return measurements
