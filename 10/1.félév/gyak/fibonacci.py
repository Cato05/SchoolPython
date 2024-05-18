def fibSequence(end):
    first = 1
    sec = 1
    third = int(1)
    
    l = []
    l.append(0)
    l.append(first)
    l.append(sec)
    k = 0

    while(end <= third - 1):
        third = first + sec
        first = sec
        sec = third
        l.append(third)
        k+= 1
        print(l)

fibSequence(15)