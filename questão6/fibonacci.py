count =  0
def rec_fib(n):
    global count
    count += 1
    if(count == 1):
        print()
    else: 
        print(f"Chamada para f({n})")

    if n == 0 or n == 1:
        return n
    else:
        return rec_fib(n - 1) + rec_fib(n - 2)

result = rec_fib(4)
print("Resultado =", result)