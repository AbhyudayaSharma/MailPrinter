import json
import sys


def get_config():
   
    with open('config.json', 'r') as f:
        try:
            data = json.load(f)
            return data
        except Exception:
            print('Invalid configuration detected!', file=sys.stderr)
            sys.exit(-1)
