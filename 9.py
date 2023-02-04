

def xlsxToTxt(text: str = '9_.txt'):
	arr, arr2 = [], []
	with open(text) as t:
		for x in t.readlines():
			arr += x.split('\t')
		for el in arr:
			z = el.replace('\n', '')
			arr2.append(float(z.replace(',', '.')))
	return arr2

def main():
	mass = xlsxToTxt()
	cen =  round(sum(mass) / len(mass), 1)
	print(cen, min(mass))
	return len([i for i in mass if i < cen and i > min(mass)*2])

print(main())
