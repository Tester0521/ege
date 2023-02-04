from itertools import product as pr

def _2(vrai: bool=True) -> str:

	print("x y z w")

	for x in 0,1:
		for y in 0,1:
			for z in 0,1:
				for w in 0,1:
					F = ((not(x and not(y)) or (not(z) or not(w))) and ((not(w) or x) or y))
					if vrai:
						if F:
							print(x, y, z, w)
					else:
						if not(F):
							print(x, y, z, w)

print('300iq ->\n' + 'x y z w\n' + ''.join([f'{x} {y} {z} {w}\n' for x, y, z, w in pr('01', repeat=4) if ((w <= x) and ((y <= z) == (x <= y)))]))

if __name__==__main__:
	_2(False)

