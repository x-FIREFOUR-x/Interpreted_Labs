x1 = float(input('Введіть координату x першої вершини: '))
y1 = float(input('Введіть координату y першої вершини: '))
x2 = float(input('Введіть координату x другої вершини: '))
y2 = float(input('Введіть координату y другої вершини: '))
x3 = float(input('Введіть координату x третьої вершини: '))
y3 = float(input('Введіть координату y третьої вершини: '))

ab =((x1-x2)**2 + (y1-y2)**2)**(1/2)   # обрахунок довжини 1-ої сторони трикутника 
bc =((x2-x3)**2 + (y2-y3)**2)**(1/2)   # обрахунок довжини 2-ої сторони трикутника 
ca =((x3-x1)**2 + (y3-y1)**2)**(1/2)   # обрахунок довжини 3-ої сторони трикутника 


if (ab + bc > ca) and (bc + ca > ab) and (ca + ab > bc):          # перевірка існування трикутника
    P = ab + bc + ca                                              # обрахунок периметра трикутника
    S = ((P/2) * (P/2 - ab) * (P/2 - bc) * (P/2 - ca)) ** (1/2)   # обрахунок площі трикутника
    print ("Периметр трикутника = %.2f" % P)
    print ("Площа трикутника = %.2f " % S)
else:
    print ("Трикутник не існує")