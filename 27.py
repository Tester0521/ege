from itertools import product as pr



'''def _27a(s = open('./src/27_B.txt').readlines()[1:], k = 109) -> list: \
return sum([max([sum(elem) for elem in pr(list(map(int, el[:-1].split())))]) for el in s]) if \
sum([max([sum(elem) for elem in pr(list(map(int, el[:-1].split())))]) for el in s]) % k != 0 else \
list(filter(lambda x: x % k != 0, [ (sum([max([sum(elem) for elem in pr(list(map(int, el[:-1].split())))]) for el in s]) - \
[max([sum(elem) for elem in pr(list(map(int, el[:-1].split())))]) for el in s][gi] + \
[sorted([sum(elem) for elem in pr(list(map(int, el[:-1].split())))])[1] for el in s][gi]) \
for gi, g in enumerate( [max([sum(elem) for elem in pr(list(map(int, el[:-1].split())))]) for el in s] ) \
if g < (sum([max([sum(elem) for elem in pr(list(map(int, el[:-1].split())))]) for el in s]) // \
len([max([sum(elem) for elem in pr(list(map(int, el[:-1].split())))]) for el in s])) ])) '''
#[max([sum(elem) for elem in pr(list(map(int, el[:-1].split())))]) for el in s][:5] if z < \
#sum([max([sum(elem) for elem in pr(list(map(int, el[:-1].split())))]) for el in s]) // \
#len([max([sum(elem) for elem in pr(list(map(int, el[:-1].split())))]) for el in s])  


def _27a(s = open('./src/27_A.txt').readlines()[1:], k = 109) -> list: \
return sum([max([sum(elem) for elem in pr(list(map(int, el[:-1].split())))]) for el in s]) if \
sum([max([sum(elem) for elem in pr(list(map(int, el[:-1].split())))]) for el in s]) % k != 12 else \
list(filter(lambda x: x % k != 0, [ (sum([max([sum(elem) for elem in pr(list(map(int, el[:-1].split())))]) for el in s]) - \
[max([sum(elem) for elem in pr(list(map(int, el[:-1].split())))]) for el in s][\
sorted([sorted([sum(elem) for elem in pr(list(map(int, el[:-1].split())))])[1] for el in s])[j] ] + \
sorted([sorted([sum(elem) for elem in pr(list(map(int, el[:-1].split())))])[1] for el in s])[j]) \
for j in range(5) ])) 


# if \
# (sum([max([sum(elem) for elem in pr(list(map(int, el[:-1].split())))]) for el in s]) - \
# [max([sum(elem) for elem in pr(list(map(int, el[:-1].split())))]) for el in s][i] + \
# [sorted([sum(elem) for elem in pr(list(map(int, el[:-1].split())))])[1] for el in s][i]) % 109 != 0]


# sum([max([sum(elem) for elem in pr(list(map(int, el[:-1].split())))]) for el in s]) // \
# len([max([sum(elem) for elem in pr(list(map(int, el[:-1].split())))]) for el in s])


print(_27a())

