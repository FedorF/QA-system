import argparse
import json
import requests


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--question", type=str, default="How to use tensorflow/serving?")
    return parser.parse_args().question


if __name__ == "__main__":
    r = requests.post("http://135.181.204.59:1000/return_answer", json=json.dumps({"question": parse_args()}))
    print(r.status_code, r.reason)
    print(r.json())
