def libraryFine(d1, m1, y1, d2, m2, y2):

    # return yearn is greater than actual year fine will be 10000
    if y1 > y2:
        return 10000
    #if return month is greaterthan actuak month with in same year fine will be 500 * diff of no months late
    elif m1 > m2 and y1 == y2:
        return 500 *(m1-m2)
    #if day is greater than actual date with in same year anad same month fine will be 15 * diff of no days
    elif d1>d2 and m1 == m2 and y1 == y2:
        
        return (d1-d2)*15
    else:
        return 0
    
    
d1,m1,y1 = 4,5,2023
d2,m2,y2 = 7,5,2023
print(d1,m1,y1,d2,m2,y2)