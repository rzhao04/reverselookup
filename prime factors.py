factor = 2
n = int
n = input ("what is n: ")
while factor <= n:
    if n % factor == 0:
        print (factor)
        n = n / factor
    else:
        factor += 1
        if n % factor == 0:
            print (factor)
            n = n / factor