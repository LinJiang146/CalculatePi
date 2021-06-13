import sys
from random import uniform

def get_pi_value(n):
    sum=0
    for i in range(n):
        x=uniform(-1,1)
        y=uniform(-1,1)
        if x**2+y**2<1:
            sum+=1
    return sum/n*4


if __name__ == '__main__':
    for i in range(1, 7):
        n = 1 * 10 ** i
        pi = get_pi_value(n)
        print(f'point number {n}, pi {pi}')
    pass
