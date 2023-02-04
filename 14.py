

def to7() -> str:
	x = 49**6 * 7**19 - 7**9 - 21
	s, a = '', '0123456789'
	while x > 0:
		x, y = divmod(x, 7)
		s += a[y]
	return s.count('6')
print(to7())