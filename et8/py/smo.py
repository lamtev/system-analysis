def c(n):
    res = 1
    mult = 9
    for i in range(1, n + 1):
        res *= mult
        mult -= 1
    res /= (2 ** (n - 1))
    return res


for i in range(1, 10):
    print(c(i))

lam = 0.05
mu0 = 0.5
mu1 = 1.25 * mu0

c1 = 9 * lam ** 1 / mu0 ** 1
c2 = 36 * lam ** 2 / mu0 ** 2
c3 = 126 * lam ** 3 / mu0 ** 3
c4 = 378 * lam ** 4 / mu0 ** 4
c5 = 945 * lam ** 5 / mu0 ** 5
c6 = 1890 * lam ** 6 / mu0 ** 6
c7 = 2835 * lam ** 7 / mu0 ** 7
c8 = 2835 * lam ** 8 / mu0 ** 7 / mu1 ** 1
c9 = 1417.5 * lam ** 9 / mu0 ** 7 / mu1 ** 2
p0 = 1 / (1 + c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9)
p1 = p0 * c1
p2 = p0 * c2
p3 = p0 * c3
p4 = p0 * c4
p5 = p0 * c5
p6 = p0 * c6
p7 = p0 * c7
p8 = p0 * c8
p9 = p0 * c9

ps = [p0, p1, p2, p3, p4, p5, p6, p6, p8, p9]

print(sum(ps))

i: int = 0
for p in ps:
    print('P{i} = {p}'.format(i=i, p=p))
    i += 1

print('Вероятность, что все машины работают и механики отдыхают = {p}'.format(p=p0))

lam_av = 0
for n in range(0, 10):
    lam_av += (9 - n) / 9 * ps[n] * lam

print('not_lambda = {x}'.format(x=lam_av))

n0_av = 0
for n in range(3, 10):
    n0_av += (n - 2) * ps[n]
print('Среднее число ожидающих ремонта машин = {x}'.format(x=n0_av))

j_av = 0
for n in range(1, 10):
    j_av += n * ps[n]
print('Среднее число машин в системе = {x}'.format(x=j_av))

t0_av = n0_av / lam_av
print('Среднее время ожидания начала ремонта = {x}'.format(x=t0_av))

t_av = j_av / lam_av
print('Среднее время нахождения в системе = {x}'.format(x=t_av))

k3 = ps[1] + 2 * sum(ps[2:9])
print(k3)

t_o = (j_av - k3) / lam_av / (9 - j_av)
print(t_o)


mu_av = 0
i = 0
for p in ps:
    mu_av += p * (mu0 if i < 7 else mu1)
    i += 1
print(mu_av)

x_av = 1 / mu_av
print(x_av)

t_c = t_o + x_av
print(t_c)
