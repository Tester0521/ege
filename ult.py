from math import ceil

def rocks19(plus:  int = 1, inc: int = 2, win: int = 129):
	for el in range(1, win - 1):
		if el * inc >= win:
			return el-plus

def rocks20(plus:  int = 1, inc: int = 2, win: int = 129):
	for el in range(1, win - 1):
		if el * inc > win // inc and el + plus > win // inc:
			return f'{min([el - plus, el // inc])}{max([el - plus, el // inc])}'

def rocks21(plus:  int = 1, inc: int = 2, win: int = 129):
	for el in range(1, win - 1):
		if el*inc > win // 2: 
			if (el+plus) * inc == win // 2:
				return el
			elif el + (plus*3) > win // 2:
				return el
# print(rocks19())
# print(rocks20())
# print(rocks21())

def f1(n): return n + 1
def f2(n): return n * 2
def f3(n): return n + 2

'''def press_f(vic: int, arr: list) -> list:
	res1, res2, res3 = 0, 0, 0
	for s in range(1, vic - 1):
		for f in arr:
			def _19_():
				for f2 in arr:
		    		if f2(f(s)) > vic // 2:
		    			res1 = s - 1
		    			break
		    def _20_():
		    	for f2 in arr:
		    		if f2(f(s)) '''
		    
# print(press_f(27, [f1, f2, f3], 2, 3))


'''def gg(vic: int, **fs) -> list:
	res1 = ceil(27 * 0.5**2)
	res2 = f'{ceil(27*0.5)-1-2}{ceil(27*0.5)-1-1}'  if 27%2!=0  \
			else f'{(ceil(27*0.5)-1)*0.5}{ceil(27*0.5)-1-2}'
	res3 = ceil(27*0.5)-1-2-1  if 27%2!=0  \
			else (ceil(27*0.5)-1)*0.5-1
	return [res1, res2, res3]'''
# V2.0
# n1, n2, n3, mx= 1, 2, 0.5, 27 
n1, n2, n3, mx= 1, 2, 0.5, 42
print(ceil(mx * n3**2), "|||", f'{ceil(mx*n3)-n1-n2}{ceil(mx*n3)-n1-n1}'  if mx%2!=0  \
			else f'{int((ceil(mx*n3)-n1)*n3)}{ceil(mx*n3)-n1-n2} (вот еще -> {ceil(mx*n3)-n1-n1})', \
			"|||", ceil(mx*n3)-n1-n2-n1  if mx%2!=0  \
			else (int((ceil(mx*n3)-n1)*n3-n1)))

# V1.0 28059-61
'''print(ceil(27 * 0.5**2), f'{ceil(27*0.5)-1-2}{ceil(27*0.5)-1-1}'  if 27%2!=0  \
			else f'{(ceil(27*0.5)-1)*0.5}{ceil(27*0.5)-1-2}', \
			ceil(27*0.5)-1-2-1  if 27%2!=0  \
			else (ceil(27*0.5)-1)*0.5-1 )'''






