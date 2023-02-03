from itertools import product as pr

def alpha(s: str = 'АБВГ', rep: int = 5) -> int: return len([x for x in pr(s, repeat = rep) if x.count("А") == 1])

print(alpha())