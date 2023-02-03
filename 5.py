from itertools import product as pr

def gen(n: int, x: int) -> str: return [f'{s[0]}{s[1]}{s[2]}{s[3]}' for s in pr('0123456789', repeat=n) if f'{int(s[2]) + int(s[3])}{int(s[0]) + int(s[1])}' == str(x)][-1]

print(gen(4, 117))