from itertools import product as pr
from numpy import ceil

def gg(x): return x+1
def ggg(x): return x+2
def gggg(x): return x*2
def gp(x): return x*3


# 19 НЕУДАЧНЫЙ ХОД ПЕТИ
def letsgo(smx: int, mx: int, fs: list): return list(filter(lambda x: x, [ [ [el[0](el[1](i)), el[1](i), i][::-1] for el in pr(fs, repeat = 2) if [el[0](el[1](i)), el[1](i), i][::-1][-1] >= mx] for i in range(1, smx//2) ]))[0][0][0]
# ИЛИ
def letsgoo(): return int(ceil((52-5)/3**2))

# 20-21
def subf(x: int, y: int, mx: int, dfS: list, op: list, c = 1): 
	if c == dfS[1] and x + y >= mx: return 1
	elif (c == dfS[1] and x + y < mx) or (c < dfS[1] and x + y >= mx): return 0
	else: return subf(x + op[0], y, mx, dfS, op, c + 1) or subf(x * op[-1], y, mx, dfS, op, c + 1) or \
				 subf(x, y + op[0], mx, dfS, op, c + 1) or subf(x, y * op[-1], mx, dfS, op, c + 1) if c % 2 != 0 else \
				 subf(x + op[0], y, mx, dfS, op, c + 1) and subf(x * op[-1], y, mx, dfS, op, c + 1) and \
				 subf(x, y + op[0], mx, dfS, op, c + 1) and subf(x, y * op[-1], mx, dfS, op, c + 1)

def subf2(x: int, y: int, mx: int, dfS: list, op: list, c = 1): 
	if (c == dfS[0] or c == dfS[-1]) and x + y >= mx: return 1
	elif (c == dfS[-1] and x + y < mx) or (c < dfS[-1] and x + y >= mx): return 0
	else: return subf2(x + op[0], y, mx, dfS, op, c + 1) or subf2(x * op[-1], y, mx, dfS, op, c + 1) or \
				 subf2(x, y + op[0], mx, dfS, op, c + 1) or subf2(x, y * op[-1], mx, dfS, op, c + 1) if c % 2 == 0 else \
				 subf2(x + op[0], y, mx, dfS, op, c + 1) and subf2(x * op[-1], y, mx, dfS, op, c + 1) and \
				 subf2(x, y + op[0], mx, dfS, op, c + 1) and subf2(x, y * op[-1], mx, dfS, op, c + 1)

def subf3(x: int, y: int, mx: int, dfS: list, op: list, c = 1): 
	if c == dfS[0] and x + y >= mx: return 1
	elif (c == dfS[0] and x + y < mx) or (c < dfS[0] and x + y >= mx): return 0
	else: return subf3(x + op[0], y, mx, dfS, op, c + 1) or subf3(x * op[-1], y, mx, dfS, op, c + 1) or \
				 subf3(x, y + op[0], mx, dfS, op, c + 1) or subf3(x, y * op[-1], mx, dfS, op, c + 1) if c % 2 == 0 else \
				 subf3(x + op[0], y, mx, dfS, op, c + 1) and subf3(x * op[-1], y, mx, dfS, op, c + 1) and \
				 subf3(x, y + op[0], mx, dfS, op, c + 1) and subf3(x, y * op[-1], mx, dfS, op, c + 1)

#20
def letsgo2(mx, dm, opers=[1, 2], dfS=[3,4,5]): return [i for i in range(1, mx//2) if subf(i, dm, mx, dfS, opers) == 1], min([i for i in range(1, mx//2) if subf2(i, dm, mx, dfS, opers) == 1 or subf3(i, 7, mx, dfS, opers) == 1])

print('19-21 V1 -->')
print(letsgoo(), end = ' (2-й способ) --> ') # 6
print(letsgo(46, 52-5, [ggg, gp])) # 6
print(letsgo2(52, 5, [2, 3]), end = '\n\n') # 5613, 14

print('19-21 V2 -->')
print(int(ceil((117-13)/2**2)), end = ' (2-й способ) --> ') # 26
print(letsgo(103, 117-13, [gg, gggg])) # 26
print(letsgo2(117, 13, [1, 2]), end = '\n\n') # 4551, 44



