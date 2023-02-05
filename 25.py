

def _25(n: int = 452_021) -> list: return [ [ x, max([(el + x // el) for el in range(2, round(x**0.5)+1) \
if x % el == 0 and (el + x // el) % 7 == 3])] for x in range(n+1, n+200) if len([(el + x // el) for el in \
range(2, round(x**0.5)+1) if x % el == 0 and (el + x // el) % 7 == 3]) > 0][:10]

print(_25())

