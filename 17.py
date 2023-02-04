
# print(_17v2())
# print(len([[s[x]+s[y] for y in range(x, len(s)) if (s[x] - s[y]) % 2 == 0 and (s[x] % 19 == 0 or s[y] % 19 == 0)] for x in range(len(s)-1)]))
def _17_300iq(s: list=[int(el) for el in open('./src/17.txt')]) -> list: return [len(f'{[[s[x]+s[y] for y in range(x+1, len(s)) if (s[x] - s[y]) % 2 == 0 and (s[x] % 19 == 0 or s[y] % 19 == 0)] for x in range(len(s)-1)]}'.replace('[', '').replace(']', '').replace(',', '').split()), max([int(el) for el in f'{[[s[x]+s[y] for y in range(x+1, len(s)) if (s[x] - s[y]) % 2 == 0 and (s[x] % 19 == 0 or s[y] % 19 == 0)] for x in range(len(s)-1)]}'.replace('[', '').replace(']', '').replace(',', '').split()])]

print(_17_300iq())









































########################################################################################################################################
########################################################		МУСОР		############################################################
########################################################################################################################################


def _17(s: str = './src/17.txt') -> list: 
	# pair = [[int(el), int(el2)] for el, el2 in zip(open('./src/17.txt').readlines()[::2], open('./src/17.txt').readlines()[1::2]) if abs((int(el) - int(el2))) % 2 == 0 and (int(el) % 19 == 0 or int(el2) % 19 == 0)]
	# pair = [[x, y] for x in [int(y) for y in open(s)] if abs(x - y) % 2 == 0 and (x % 19 == 0 or y % 19 == 0)]
	pair = [[x, y]]
	ms = sum(pair[-1])
	return [len(pair), ms]

# print(_17())
'''arr = []
t = open('./src/17.txt').readlines()
for el in t[1::]:
	for el2 in t[:-1]:
		if abs(int(el) - int(el2)) % 2 == 0 and (int(el) % 19 == 0 or int(el2) % 19 == 0):
			arr.append([el, el2])
print(len(arr))'''



'''count = m = 0
for x in range(len(s)-1):
	for y in range(x+1, len(s)):
		if (s[x] - s[y]) % 2 == 0 and (s[x] % 19 ==0 or s[y] % 19 == 0):
			count += 1
			m = max(m, s[x] + s[y])'''

'''for x in s[:-1]:
	for y in s[x+1:]:
		if (x - y) % 2 == 0 and (x % 19 == 0 or y % 19 == 0):
			count += 1
			m = max(m, x+y)

print(count, m)'''
# print([x for x in pr([x for x in s[:-1]], [y for y in s[1:]], repeat=2)])
# def _17v2(l: list) -> str: return [[i for i in range(len(l)-1) if (l[i] - l[j]) % 2 == 0 and (l[i] % 19 == 0 or l[j] % 19 == 0)]
# return [[len(x), max(sum(x))] for x in [[el[0].replace('\n', ''), el[-1].replace('\n', '')]  for el in pr(open('./src/17.txt').readlines(), repeat = 2)] if (int(x[0]) - int(x[-1])) % 2 == 0 and (int(x[0]) % 19 == 0 or int(x[-1]) % 19 == 0)]

