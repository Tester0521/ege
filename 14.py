

def to7(x: int, b: int, al: str = '0123456789', fut = []) \
		-> list: return fut.count(f'{b-1}') if x <= 0 else \
		to7( x//b, b, fut = fut + [al[x%b]] )
		
print(to7(49**6 * 7**19 - 7**9 - 21, 7))

