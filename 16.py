import sys
sys.setrecursionlimit(9999999)

def _16(n):
	if n == 0: return 0
	if n % 3 == 0 and n > 0: return n + _16(n - 3)
	if n % 3 > 0: return n + _16(n - (n % 3))

print(_16(22))