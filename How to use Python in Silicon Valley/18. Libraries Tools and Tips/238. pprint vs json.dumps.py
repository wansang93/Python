import json
import pprint

l = ['apple', 'orange', 'banana', 'peach', 'mango']
l.insert(0, l[:])
l.insert(0, l[:])
l.insert(0, l[:])
l.insert(0, l[:])
pp = pprint.PrettyPrinter(
    indent=4, width=40, compact=True, depth=2)
pp.pprint(l)
# [   [   [...], [...], [...], 'apple',   
#         'orange', 'banana', 'peach',    
#         'mango'],
#     [   [...], [...], 'apple', 'orange',
#         'banana', 'peach', 'mango'],    
#     [   [...], 'apple', 'orange',       
#         'banana', 'peach', 'mango'],    
#     [   'apple', 'orange', 'banana',    
#         'peach', 'mango'],
#     'apple', 'orange', 'banana',
#     'peach', 'mango']

d = {'A': 'a', 'B': 'b', 'C': {'D': 'd', 'E': 'e'}}
pp2 = pprint.PrettyPrinter(indent=4, width=40)
pp2.pprint(d)
# {   'A': 'a',
#     'B': 'b',
#     'C': {'D': 'd', 'E': 'e'}}

print(json.dumps(d, indent=4))
# {
#     "A": "a",
#     "B": "b",
#     "C": {
#         "D": "d",
#         "E": "e"
#     }
# }

# https://docs.python.org/3/library/pprint.html -> example
import json
import pprint
from urllib.request import urlopen
with urlopen('https://pypi.org/pypi/sampleproject/json') as resp:
    project_info = json.load(resp)['info']

print(json.dumps(project_info, indent=4))