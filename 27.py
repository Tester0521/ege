from itertools import product as pr
import numpy as np



def _27a(s = open('./src/27_B.txt').readlines()[1:], k = 109) -> list: \
return sum([max([elem for elem in list(map(int, el[:-1].split()))]) for el in s]) if \
sum([max([elem for elem in list(map(int, el[:-1].split()))]) for el in s]) % k != 0 else \
\
list(filter(lambda x: x % k != 0, [ (sum([max([elem for elem in list(map(int, el[:-1].split()))]) for el in s]) - \
g[2] + g[1]) \
for gi, g in enumerate( sorted( [sorted(list(map(int, el[:-1].split()))) for el in s ][:200], key=sum)  ) \
 ])) 




print(_27a())

