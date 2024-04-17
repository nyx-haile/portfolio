import itertools
import math

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 23
def comb(numbers, target):
    return [seq for i in range(len(numbers), 0, -1) for seq in itertools.combinations(numbers, i) if sum(seq) == target]

def freq(lis):
    results = {}
    for item in lis:
        for num in item:
            try:
                results[num] +=1
            except:
                results[num]=1
    return results


print(freq(comb(numbers, target)), 'Original')


agg = []
numbersm = [1, 3, 5, 8, 6, 9]

for num in numbersm:
    newnum = numbersm.copy()
    newnum.remove(num)
    agg.extend(comb(newnum, target-num))
    print(freq(comb(newnum, target-num)), 'Minus '+str(num))

print(freq(agg))
sum = 0
for values in freq(agg).values():
    sum += values

print('SUM: ', sum)

fragg = freq(agg)

sumi =0
nrfragg ={}
for key in fragg.keys():
    nrfragg[key] = fragg[key]*1000/sum-math.floor(fragg[key]*1000/sum)
    fragg[key] = math.floor(fragg[key]*1000/sum)
    sumi += fragg[key]
print(fragg)
print(nrfragg, 1000-sumi)
