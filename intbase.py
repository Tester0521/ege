def base(num, fn, tn):
    n = int(num, fn) if isinstance(int, str) else num
    alp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        n, m = divmod(n, tn)
        res += alp[m]
    return res[::-1]