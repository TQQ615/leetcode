def gd():
    x0 = 10
    step = 0.001
    for i in range(100):
        gd_ = 4 * x0 * (x0 * x0 - 3)
        x = x0 - step * gd_
        x0 = x

    return x0

def gradient_descent(y):
    x = 10
    alpha = 0.001
    deta = 1
    count = 1
    while abs(deta)>0.001:
        deta = 4*x*(x*x-y)
        x -= alpha*deta
        count = count+1
    return x

print(gd())
# print(gradient_descent(3))
