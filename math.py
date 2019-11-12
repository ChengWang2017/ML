def set_x(a,b,c,d) :
    x = 1000*a + 100*b + 10*c + d
    return x
def set_y(a,b,c,d) :
    y = c
    return y
def set_z(a,b,c,d) :
    z = 1000*c + 100*a + 10*b + b


for a in range(10) :
    for b in range(10) :
        for c in range(10) :
            for d in range(10) :
                for e in range(10) :
                    for f in range(10) :
                        x = 100000*a + 10000*b + 1000*c + 100*d + 10*e + f
                        y = 3
                        z = 100000*b + 10000*c + 1000*d + 100*e + 10*f + a
                        if (x*y == z) and (a!=b) and (a!=c) and (a!=d) and (b!=c) and (b!=d) and (c!=d) :
                            print(x,"*",y,"=",z)
                            print(a,b,c,d,e,f)
                    
