def pytho_sum(_sum):
    a = 0
    b = 0
    c =0
    for a in range(_sum//3):
        for b in range(_sum):
            c = _sum - (a + b)
            if (a*a + b*b == c*c) and a != 0:
                product = a * b * c
                print(a, b, c)
                return product
            
print(pytho_sum(1000))