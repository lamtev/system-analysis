import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def fact(n):
    if n == 0:
        return 1
    else:
        return fact(n - 1) * n


def p0(k, m, lam, mu):
    rho = lam / mu
    rhoc = rho / k
    s = 0
    for i in range(1, k + 1):
        s += ((rho ** i) / fact(i))
    right = (rho ** (k + 1) * (1 - rhoc ** m)) / (fact(k) * (1 - rhoc) * k)
    return (1 + s + right) ** (-1)


def potk1(k, m, lam, mu):
    rho = lam / mu
    return rho ** (k + m) * p0(k, m, rho, mu) / k ** m / fact(k)


def n01(k, m, lam, mu):
    rho = lam / mu
    rhoc = rho / k
    return rho ** (k + 1) * p0(k, m, rho, mu) * (1 - rhoc ** m * (m + 1 - m * rhoc)) / k / (1 - rhoc) ** 2 / fact(k)


def to1(k, m, lam, mu):
    rho = lam / mu
    return n01(k, m, rho, mu) / rho / mu


def tc1(k, m, lam, mu):
    rho = lam / mu
    return to1(k, m, rho, mu) + 1 / mu * (1 - potk1(k, m, rho, mu))


def to2(m, lam, mu):
    rho = lam / mu
    return (rho * (1 - rho ** m) * (1 + m - m * rho)) / (mu * (1 - rho) * (1 - rho ** (m + 2)))


def tc2(m, lam, mu):
    rho = lam / mu
    return ((1 - rho ** (m + 1)) * (2 + m - rho - m * rho)) / (mu * (1 - rho) * (1 - rho ** (m + 2)))


mu0 = 100
lams = np.linspace(0.001, mu0 * 4, 1000)
to1s = []
tc1s = []
to2s = []
tc2s = []

for l in lams:
    to1s.append(to1(4, 4, l, mu0))
    tc1s.append(tc1(4, 4, l, mu0))
    to2s.append(to2(4, l, 4 * mu0))
    tc2s.append(tc2(4, l, 4 * mu0))

mpl.rcParams['figure.figsize'] = [8, 6]
mpl.rcParams['figure.dpi'] = 100
mpl.rcParams['grid.alpha'] = 0.3

plt.plot(lams, to1s, 'b',
         label='M/M/4/4, $\mu={mu}$, $t_{i} \in [{a:0.1e}, {b:0.1e}]$'.format(mu=mu0, i='{ож}', a=to1s[0], b=to1s[-1]))
plt.plot(lams, to2s, 'r', label='M/M/1/4, $\mu={mu}$'.format(mu=4 * mu0))
plt.xlabel('$\lambda$', fontsize=12)
plt.ylabel('$t_{ож}$', fontsize=12)
plt.xlim((min(lams), max(lams)))
plt.grid(True)
plt.legend()
plt.show()

plt.plot(lams, tc1s, 'b',
         label='M/M/4/4, $\mu={mu}$, $t_{i} \in [{a:0.1e}, {b:0.1e}]$'.format(mu=mu0, i='{с}', a=tc1s[0], b=tc1s[-1]))
plt.plot(lams, tc2s, 'r', label='M/M/1/4, $\mu$={mu}'.format(mu=4 * mu0))
plt.xlabel('$\lambda$', fontsize=12)
plt.ylabel('$t_{с}$', fontsize=12)
plt.xlim((min(lams), max(lams)))
plt.grid(True)
plt.legend()
plt.show()
