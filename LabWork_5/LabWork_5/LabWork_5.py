p = int(input('input first number: '))
q = int(input('input second number: '))
print('mutually prime divisors of the p with the q:',end=' ')
for i in range (1, p+1):
    if p % i == 0:
        simple = True
        j = 2
        while (j <= i) and (simple):
            if (i % j == 0) and (q % j == 0):
                simple = False
            j= j + 1
        if (simple):
            print(i, end=' ')
print() 
