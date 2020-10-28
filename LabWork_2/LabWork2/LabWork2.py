x= float(input('input coordinate of points (x): '))         # coordinate x of dot
y= float(input('input coordinate of points (y): '))         # coordinate y of dot

if  (x >= -1) and (x <= 1) and (y**2 <= 4 - (x - 1)**2):          # the condition of belonging to the area is limited to 1-th schedule   
    print ('belong to shape')
else:
    if  (x > 1) and (x <= 3) and (abs(y) <= -x + 3):              # the condition of belonging to the area is limited to 2-th schedule
        print ('belong to shape')
    else:
        print ('no belong to shape')

