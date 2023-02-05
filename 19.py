from math import ceil


#######################################################################################################################
########################################		19		###############################################################
########################################  2/3 действия  ###############################################################

########		НЕУДАЧНЫЙ ХОД ПЕТИ		########

def _19_1(mx, p, n1, n2=0) -> int: return int(ceil(mx/p**2))

########		ЛЮБОЙ ХОД ПЕТИ		########		

def _19_2(mx, p, n1, n2=0) -> int: return int(ceil(mx/p-n1))

#######################################################################################################################
########################################		20		###############################################################
########################################	2 действия  ###############################################################
# Найдите два таких значения S, при которых у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:
# — Петя не может выиграть за один ход;
# — Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.

def _20_1(mx, p, n1) -> str: return f'{int((ceil(mx / p)-n1)/p)}{ceil(mx/p)-n1*2}'

########################################	3 действия  ###############################################################
def _20_2(mx, p, n1, n2=0) -> str: return f"{ceil(mx/p)-n1-n2}{ceil(mx/p)-n1-n1}"  #if mx%2!=0  \
			#else f"{int((ceil(mx/p)-n1)/p)} {ceil(mx/p)-n1-n2} (вот еще -> {ceil(mx/p)-n1-n1})"

#---------------------------------------	3 значения ---------------------------------------------------------------#

def _20_3(mx, p, n1, n2=0) -> str: return f"{int((ceil(mx/p)-n1)/p)}{ceil(mx/p)-n1-n2} {ceil(mx/p)-n1-n1}"

#######################################################################################################################
########################################		21		###############################################################
########################################	2 действия  ###############################################################
# Найдите минимальное значение S, при котором одновременно выполняются два условия:
# — у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
# — у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.

def _21_1(mx, p, n1) -> int: return int((ceil(mx/p)-n1)/p-n1) if ((ceil(mx/p)-n1*2)/p)*p**3 < mx \
										else int((ceil(mx/p)-n1)-n1*2)

########################################	3 действия  ###############################################################

def _21_2(mx, p, n1, n2=0) -> int: return int((ceil(mx/p)-n1)/p-n1) if ((ceil(mx/p)-n1-n2)/p)*p**3 < mx \
										else int((ceil(mx/p)-n1)-n2-n1)

'''print('TESTS -->')
print('2 ДЕЙСТВИЯ >>')
print('№28145')
print(_19_1(94, 2, 1), end = '  ||  ')
print(_20_1(94, 2, 1), end = '  ||  ')
print(_21_1(94, 2, 1))
print('№28155')
print(_19_1(22, 2, 1), end = '  ||  ')
print(_20_1(22, 2, 1), end = '  ||  ')
print(_21_1(22, 2, 1))
print('3 ДЕЙСТВИЯ >>')
print('№27832')
print(_19_1(52, 2, 1, 4), end = '  ||  ')
print(_20_2(52, 2, 1, 4), end = '  ||  ')
print(_21_2(52, 2, 1, 4))
print('№27848')
print(_19_1(54, 2, 1, 3), end = '  ||  ')
print(_20_3(54, 2, 1, 3), end = '  ||  ')
print(_21_2(54, 2, 1, 3))'''


# 27802-4
# print(_19_1(68, 5, 1, 4))
# print(_20_2(68, 5, 1, 4))
# print(_21_2(68, 5, 1, 4))

print(_19_1(94, 2, 1))
print(_20_1(94, 2, 1))
print(_21_1(94, 2, 1))



