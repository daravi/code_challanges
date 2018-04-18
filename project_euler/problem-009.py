import math


def find_shit():
    while True:
        for a in range(500):
            for b in range(500):
                c = math.sqrt(a*a+b*b)
                if c - int(c) == 0 and a+b+c == 1000:
                    return (a,b,c, a*b*c)
                    
                    
print find_shit()                    