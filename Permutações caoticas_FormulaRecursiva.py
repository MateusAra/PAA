
#2) Formula Recursiva:
#an = n*an-1 + 1 n ≥ 2, n par
#an = n*an-1 - 1 n ≥ 2, n impar
#a1 = 0
#a1 = 0, pois não existe permutação caótica em 1 único elemento.


def T(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (n-1)*(T(n-1) + T(n-2))
print(T(8))
