def Cos(x, E):
    i = 2
    xn = x * x / i * (-1)
    rez1 =  1
    rez2 = rez1 + xn
    while ( abs (rez2 - rez1)>= E):
        i += 1
        xn = xn * (x * x / i /  (i + 1) ) * (-1)
        rez1 = rez2
        rez2 = rez1 + xn
    return rez2

def precision (E):
    b = 1 / E
    number = 1
    while (b > 9):
        b = b / 10
        number += 1
    return number

E = float(input('Input the accuracy of the calculation: '))
a = float(input('Input the first number a (rad): '))
b = float(input('Input the second number b (rad): '))
y = Cos(a,E) + Cos(b, E)**2 + Cos(a + b, E)
print ("y =", round(y, precision (E) ))

