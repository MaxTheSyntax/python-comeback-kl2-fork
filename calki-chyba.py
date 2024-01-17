#Sx^ndx = x^(n+1) / n+1

def prostokaty(a,b,n):
    dx = (b-a)/n
    s = 0
    for i in range(n):
        s += (a + i * dx + 3) * dx
    return s

print(prostokaty(2,6,40))