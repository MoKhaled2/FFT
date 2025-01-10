import math

class Complex:
    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __str__(self):
        if self.real == 0:
            return f"{self.imag:.2f}i"
        elif self.imag > 0:
            return f"{self.real:.2f} + {self.imag:.2f}i"
        elif self.imag == 0:
            return f"{self.real:.2f}"
        else:
            return f"{self.real:.2f} - {-self.imag:.2f}i"

def operation(x,res,step):
    for k in range(0, step, 2):
        x[k] = res[k]
        x[k + 1] = res[k + step]
    for j in range(1, step+ 1, 2):
        x[j + step- 1] = res[j]
        x[j + step] = res[j + step]
    return x

def twiddle_factor(step, total_steps):
    angle = -2 * math.pi * step / total_steps
    return Complex(math.cos(angle),math.sin(angle))

def FFT(input_signal):
    if len(input_signal)==2:
        num=input_signal[1]
        input_signal[1] = input_signal[0] - input_signal[1]
        input_signal[0]=num+input_signal[0]
        return input_signal
    if len(input_signal)==1:
        input_signal.append(input_signal[0])
        return input_signal

    while len(input_signal) != 2**math.floor(math.log2(len(input_signal))):
        input_signal.append(0)
    n = len(input_signal)

    x = [Complex(val) for val in input_signal]
    res = [x[j] for j in range(len(x))]

    step = len(x)//2
    x = operation(x,res,step)

    step = 1
    while step < n:
        half_step = step
        for start in range(0, n, step * 2):
            for k in range(half_step):
                twiddle = twiddle_factor(k, step * 2)
                temp = twiddle * x[start + k + half_step]
                x[start + k + half_step] = x[start + k] - temp
                x[start + k] = x[start + k] + temp
        step *= 2

    return x

if __name__ == "__main__":
    n=int(input('How many N  do you Want do enter  '))
    signal = []
    i=1
    while n:
        num=int(input(f"enter {i} number "))
        signal.append(num)
        n-=1
        i+=1
    # signal = [1,-1,0,1,2,0,0,1]

    result = FFT(signal)
    i=0
    print("-------------")
    print("|  NO NAME  |")
    print("-------------\n\n")

    print("THE RESULT IS :")
    print('-'*30)
    for r in result:
        print(f'|  X[{i}] = {r}')
        i+=1
    print('-'*30)
