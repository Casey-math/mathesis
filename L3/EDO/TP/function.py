import numpy as np

def euler_exp(t0,y0,T,h,f):
    """
    cette fonction approche la solution d'un problème de cauchy par la méthode d'Euler explicite
    elle mange (t0,y0,T,h,f)
    et retourne t, y
    """
    t = np.arange(t0, t0+T+h,h)
    y = t*0
    y[0] = y0
    for i in range(len(t)-1):
        y[i+1] = y[i] + h*f(t[i],y[i])
    return t, y
