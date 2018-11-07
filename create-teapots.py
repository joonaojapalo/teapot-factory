import math
import random
import pprint

def pick(l, idx):
    return [e for (i,e) in enumerate(l) if i in idx]

def rand(k, eps):
    return sum([random.randint(-eps, eps) for n in range(k)])

shifts=[]
N=52
w=[21,25,24,12,19,21,25,20,22,21,23]
eps=5
ws=list(range(len(w)))
for i in range(N):
    nw = random.randint(4,5)
    random.shuffle(ws)
    p=ws[:nw]
    shifts.append({
        "shift": i,
        "workers": sorted(p),
        "teapots": sum(pick(w, p)) + rand(nw, eps)
    })

pprint.pprint (shifts);
