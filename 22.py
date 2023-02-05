

def _22(d: list = [[3], [5], [2,1-1,2-1], [5,3-1], [4,4-1], [2], [3,5-1], [4,4-1,5-1], [5], [8,6-1,7-1], [2,3-1,5-1], [9,2-1,7-1], [3, 11-1], [1,2-1,6-1], [2,5-1,8-1]]) -> 'hehe':
	# return [0 for xi, x in enumerate(d.values()) if x[0] <= max([h for h in [d.values()[z] for z in x[1:]]])]#  else x[0] - max([h for h in [d.values()[z] for z in x[1:]]])]
	# return [max([h[0] for h in [d[z] for z in x[1:]] if len(h) > 1]) for x in d]
	maxx = 0
	for x in d:
		for iy, y in enumerate(x):
			r = max([d[s][0] for s in x[1:] if len(x) > 1] else [maxx, 0]) 
			maxx = max(maxx, r)
	return maxx

print(_22())
