# F_i(T) = (2 k nu_i^2 / c^2) * [ T / (1 + d_i * sqrt(T)) ] * (1 - exp(-a_i * T^{b_i}))

import math
import matplotlib.pyplot as plt

kB = 1.3807e-23 # Boltzmann
c = 2.99792458e8


table = [
    # i,  nu_GHz,      ai,            bi,    di,      depth_km,  F_obs
    (1,   0.6,     2.0e-4,          1.15,  0.0025,       0,     7.59342e-21),
    (2,   1.2,     4.0e-4,          1.18,  0.0027,      50,     6.15189e-20),
    (3,   2.4,     8.0e-4,          1.20,  0.0030,     100,     3.90419e-19),
    (4,   4.8,     1.6e-3,          1.23,  0.0034,     170,     1.86758e-18),
    (5,   9.6,     3.2e-3,          1.26,  0.0036,     250,     8.12656e-18),
    (6,   22.0,    7.0e-3,          1.30,  0.0040,     375,     4.14506e-17),
]

def Fi(T, nu_Hz, a, b, d):
    pt1 = 2.0 * kB * (nu_Hz**2) / (c**2)
    pt2 = (T / (1.0 + d * math.sqrt(T)))
    pt3 = (1.0 - math.exp(-a * (T**b)))
    Function = pt1 * pt2 * pt3
    return Function

def bisect(func, target, lo, hi, args=(), tol=1e-8, max_iter=200):

    f_lo = func(lo, *args) - target
    f_hi = func(hi, *args) - target #THIS IS actually killing me wtf am i doing wrongggggg

    expand_iter = 0
    while f_lo * f_hi > 0 and expand_iter < 60:
        if f_lo < 0 and f_hi < 0:
            hi *= 2.0
            f_hi = func(hi, *args) - target
        else:
            lo *= 0.5
            if lo <= 1e-12:
                lo = 1e-12
            f_lo = func(lo, *args) - target
        expand_iter += 1
    
    for i in range(max_iter): 
        f_mid = func(0.5 * (lo + hi), *args) - target
        
        if f_lo * f_mid <= 0:
            hi = 0.5 * (lo + hi)
            f_hi = f_mid
        else:
            lo = 0.5 * (lo + hi)
            f_lo = f_mid
    
    return 0.5 * (lo + hi) 

def main():
    results = []
    for i, nu_GHz, a, b, d, depth_km, F_obs in table:
        nu_Hz = nu_GHz * 1.0e9

        T_sol = bisect(Fi, F_obs, 1e-6, 3000, args=(nu_Hz, a, b, d), tol=1e-10, max_iter=500)
        
        results.append((i, nu_GHz, depth_km, T_sol))

    # plot T vs Depth
    depths = [r[2] for r in results]
    temps  = [r[3] for r in results]

    plt.figure(figsize=(6, 4.5))
    plt.plot(temps, depths)
    plt.xlabel("temp T (K)")
    plt.ylabel("depth from 1 bar level (km)")
    plt.title("temperature v depth")
    plt.savefig("mwrTemperature.png")
    # plt.show()

if __name__ == "__main__":
    main()
