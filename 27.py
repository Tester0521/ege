from itertools import product as pr



def _27a(s = open('./src/27_A.txt').readlines()[1:], k = 109) -> list: \
return sum([max([sum(elem) for elem in pr(list(map(int, el[:-1].split())))]) for el in s]) if \
sum([max([sum(elem) for elem in pr(list(map(int, el[:-1].split())))]) for el in s]) % k != 12 else \
[sorted([sum(elem) for elem in pr(list(map(int, el[:-1].split())))])[-1] for el in s]

print(_27a())
# def _27a(s = open('./src/27_A.txt').readlines()[1:], k = 109) -> list: \
# return [sum([max([sum(elem) for elem in pr(list(map(int, el[:-1].split())))]) for el in s]), sum([max([sum(elem) for elem in pr(list(map(int, el[:-1].split())))]) for el in s]) % k != 0]

# def _27b(s = open('./src/27_B.txt').readlines()[1:], k = 109) -> list: \
# return [sum([max([sum(elem) for elem in pr(list(map(int, el[:-1].split())))]) for el in s]), sum([max([sum(elem) for elem in pr(list(map(int, el[:-1].split())))]) for el in s]) % k != 0]


# print(_27b())