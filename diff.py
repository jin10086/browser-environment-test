import json
from deepdiff import DeepDiff
from pprint import pprint

with open("normal.json") as f:
    normal = json.loads(f.read())

with open("selenuim.json") as f:
    selenuim = json.loads(f.read())

with open("pyppeteer.json") as f:
    pyppeteer = json.loads(f.read())

print("selenuim 与正常环境的差异")
print("#" * 60)
c = DeepDiff(normal, selenuim)
pprint(c, indent=2)

print("pyppeteer 与正常环境的差异")
print("#" * 60)
c1 = DeepDiff(normal, pyppeteer)
pprint(c1, indent=2)
