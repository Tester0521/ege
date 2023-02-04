import sys
sys.setrecursionlimit(9999999)

def changer(k: str, k2: str, v='111', v1='222', w='11', w1='22') -> str: \
		return [len(k), k2.replace(v, w1, 1).replace(v1, w, 1)] \
		if k2.replace(v, w1, 1).replace(v1, w, 1).count('1') == 1 \
		else changer(k=k,k2=k2.replace(v, w1, 1).replace(v1, w, 1))

print(changer('1'*104, '1'*104))



