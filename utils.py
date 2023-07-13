import json
import os
from collections import defaultdict
from typing import List, Dict


def read_files(path='./repos'):
    out:Dict[str,set] = defaultdict(set)
    comp = os.listdir(path)
    for com in comp:
        try:
            repos = os.listdir(f"{path}/{com}")
        except:
            continue
        for repo in repos:
            try:
                activity = json.loads(open(f"{path}/{com}/{repo}/activity_details.json").read())
            except:
                continue
            for k,values in activity.items():
                for v in values:
                    out[v[0]].add(repo)
    return out






if __name__ == '__main__':
    print(read_files())