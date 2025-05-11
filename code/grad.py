def gd(f, f_, lr, x0, big):
    x = x0
    oldy = None
    iter = 0
    while True:
        x = x - lr * f_(x)
        y = f(x)
        print(f"{iter} {x} {y}")
        if oldy is not None and abs(y - oldy) < big:
            break
        oldy = y
        iter += 1 
    
gd(lambda x: x*x, lambda x: 2*x, 0.1, 10, 0.1)