import json
def read_json_objects(data):
    decoder = json.JSONDecoder()
    offset = 0

    while offset < len(data):
        item = decoder.raw_decode(data[offset:])

        yield item[0]
        offset += item[1]


def give_name(item):
    return hash(tuple(item.values()))

with open('winners.txt', 'r') as f:
        winners= list(read_json_objects(f.read().replace('\n', '')))

data = winners
data.extend([{"1": 39,    "2": 11,    "3": 26,    "4": 135,    "5": 111,    "6": 126,    "7": 180,    "8": 213,    "9": 159}, {"1": 140, "2": 0, "3": 140, "4": 0, "5": 200, "6": 180, "7": 0, "8": 180, "9": 160}])
results = {}

for general in data:
    results[give_name(general)]=[general, 0]

def fight(a, b):

      for stack in a.keys():
          if a[stack] > b[stack]:
              results[give_name(a)][1]+=int(stack)
          elif a[stack] < b[stack]:
              results[give_name(b)][1]+=int(stack)

fight({"1": 39,    "2": 11,    "3": 26,    "4": 135,    "5": 111,    "6": 126,    "7": 180,    "8": 213,    "9": 159}, {"1": 140, "2": 0, "3": 140, "4": 0, "5": 200, "6": 180, "7": 0, "8": 180, "9": 160})
print(results)
