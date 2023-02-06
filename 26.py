import sys
sys.setrecursionlimit(9999999)

def _26(s = open('./src/26.txt').readlines(), mem = int(open('./src/26.txt').readlines()[0][:-1].split()[0]), x = 498):\
return [len(sorted(list((map(int, [el[:-1] for el in s][1:]))))[:-x]), \
max(sorted(list((map(int, [el[:-1] for el in s][1:]))))[:-x])] if sum(sorted(list((map(int, [el[:-1] for el in s][1:]))))[:-x])\
 <= mem else _26(x = x + 1)

print(_26())

