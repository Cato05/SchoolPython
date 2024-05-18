def prime():
    import os
    import math

    start = int(input("Kérem adjon meg egy számot, amelytől ki szeretné iratni a prímszámokat: "))
    end = int(input("Kérem adjon meg egy számot, amelyig szeretné iratni a prímszámokat: "))
    i = start

    k = 1
    n = end * end
    while start != end:
        i = 2
        while i * i <= n:
            if n / i:
                print(i)
                return False
                
            else:
                
                i += 1

        



    '''###
    for num in range(start, end +1):
        if num > 1:
            for i in range(2, int(num**0.5)+1):
                if (num % i)'''
    
prime()