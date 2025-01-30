
tol = 1e-14

def my_sqrt(x, kmax):
    s = 1.0
    for k in range(kmax):
        print(f"At each iteration {k} the value of s = {s}")
        s0 = s
        s = 0.5 * (s + (x/s))
        if(abs(s0-s) < tol):
            break
    return s
x = 2.0
print(f"square root of {x} is {my_sqrt(x, 100)}")

