
def my_sqrt(x, kmax):
    s = 1.0
    for k in range(kmax):
        s = 0.5 * (s + (x/s))
    return s

print(my_sqrt(2.0, 100))

