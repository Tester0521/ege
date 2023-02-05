

def _23(x: int, y: int) -> int:
    if x > y: return 0
    if x == y: return 1
    else: return _23(x + 2, y) + _23(x + 5, y)
print(_23(1, 20))