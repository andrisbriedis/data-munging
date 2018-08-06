from measurment import Measurement
from score import Score


def normalize_football(data):
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


def normalize(data):
    measurements = []
    for row in data[2:-1]:
        line = row.split()
        day = int(line[0])
        min = int(line[2].replace("*", ""))
        max = int(line[1].replace("*", ""))
        measurements.append(Measurement(day, min, max))
    return measurements
