import math

while True:
    try:
        A = int(input("Adj meg egy valós számot: "))
        K = int(input("Adj meg egy egész számot: "))
        break
    except ValueError:
        print("Mondom egész!")

dic = {}
dic.update({"A": A})
dic.update({"K": K})


def pow(a,b):
    if(b==0):
        return 1
         
    answer=a
    increment=a
     
    for i in range(1,b):
        for j in range (1,a):
            answer+=increment
        increment=answer
    return answer
 
# driver code
print(pow(int(dic.get("A")), int(dic.get("K"))))