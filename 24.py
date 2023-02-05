

def _24(s: str = open('./src/24.txt').readline(), f : str = 'XZZY'): return max([len(el) for el in s.split(f)])+(len(f)-1)*2

print(_24())
