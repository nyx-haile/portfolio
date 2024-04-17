import random
import itertools
import io
import json
import ast
import math

save = 0
winners = []
blotto = {"1": 140, "2": 0, "3": 140, "4": 0, "5": 200, "6": 180, "7": 0, "8": 180, "9": 160}
def read_json_objects(data):
    decoder = json.JSONDecoder()
    offset = 0

    while offset < len(data):
        item = decoder.raw_decode(data[offset:])

        yield item[0]
        offset += item[1]

with open('winners.txt', 'r') as f:
        winners= list(read_json_objects(f.read().replace('\n', '')))
        # rdfile = f.readlines()
        # for line in rdfile:
        #     line.replace('\n', '')
        #     print(line)
        #     entry=json.loads(line)
        #     winners.append(entry)
        # print(winners)
        save= len(winners)

def beat(blotto):
    result = blotto
    for item in blotto.keys():
        if result["1"] >= 1:
            result[item] = blotto[item]+1
            result["1"]-=1
    return result
def generate(amount):
    results = []
    for alphamamsndasd in range(amount):
        n=1000
        dict = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
        while n > 0:
            x = random.randint(0, 1)
            dict[f"{random.randint(1, 9)}"] += x
            n-=x
        results.append(dict)

    for sdkjfhsdkjfs in range(amount):
        n = 1000
        dict = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
        while n > 0:
            x = random.randint(0, n)
            dict[f"{random.randint(1, 9)}"] += x
            n-=x
        results.append(dict)

    for sdkjfdkjfs in range(amount):
        n = 1000
        dict = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
        while n > 0:
            x = random.randint(0, random.randint(0, n))
            dict[f"{random.randint(1, 9)}"] += x
            n-=x
        results.append(dict)
    for winner in winners:
        results.append(beat(winner))
    return results

def give_name(item):
    return hash(tuple(item.values()))

def test_blotto(n):
    blotto = {"1": 140, "2": 0, "3": 140, "4": 0, "5": 200, "6": 180, "7": 0, "8": 180, "9": 160}
    data = generate(n)
    data.append(blotto)
    data.extend(winners)
    results={}

    for general in data:
        results[give_name(general)]=[general, 0]

    def fight(a, b):

        for stack in a.keys():
            if a[stack] > b[stack]:
                results[give_name(a)][1]+=int(stack)
            elif a[stack] < b[stack]:
                results[give_name(b)][1]+=int(stack)

    counter = 0
    v =len(list(results.keys()))
    v=v*(v-1)/2
    print(v)
    c=0
    for a, b in itertools.combinations(results.keys(), 2):
        if(not c < math.floor(v/100)):
            counter+=1
            print(str(counter)+'%')
            c=0
        fight(results[a][0], results[b][0])
        c+=1
    scores = results
    sor =list(scores.values())
    sor.sort(reverse=True, key = lambda x:x[1])
    print(sor[0])
    with open('winners.txt', 'w') as f:
        for n in range(save+100):
            f.write(json.dumps(sor[n][0]).replace(',', ',\t')+'\n')

    return results

test_blotto(10000)
