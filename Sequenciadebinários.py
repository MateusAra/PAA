base=[[[-1 for i in range(2)] for j in range(2)] for k in range(32)]

def count(pos,indx,ant,bin):

    if (pos == len(bin)):
        return 1;

    if (base[pos][indx][ant] != -1):
        return base[pos][indx][ant];
 
    val = 0

    if (bin[pos] == '0'):
        val = val + count(pos + 1, indx, 0, bin)

    elif (bin[pos] == '1'):
        val = val + count(pos + 1, 1, 0, bin)

    if (ant == 0):

        if (indx == 1):
            val += count(pos + 1, indx, 1, bin)
 
        elif (bin[pos] == '1'):
            val += count(pos + 1, indx, 1, bin)

    base[pos][indx][ant] = val
    return val
    
def verificar(num):
    bin=""
    while (num > 0):
        if (num % 2):
            bin += "1"
        else:
            bin += "0"
        num //= 2   
    bin=bin[::-1];
    return count(0, 0, 0, bin)
 
if __name__ == "_main_":

    t = 3
    print("Temos {} elementos binarios que não tem 1S consecutivos".format(verificar(t)))