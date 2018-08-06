def load_test_data(filename):
    lines = []
    with open(filename) as data:
        for line in data:
            lines.append(line)

    return lines
