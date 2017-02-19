import json
import sys


def read_json(input_file):
    with open(input_file) as f:
        for line in f.readlines():
            yield json.loads(line)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('please provide json data file')
        sys.exit(1)
    input_file = sys.argv[1]
    tweets = read_json(input_file)
    for tw in tweets:
        print(dict(tw)['text'])
