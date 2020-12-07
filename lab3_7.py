import numpy as np
import matplotlib.pyplot as plt

print("Введите a:")
a = int(input())
print("Введите b:")
b = int(input())

v = np.linspace(-7, 7, 1000)  # область сетки
x1 = lambda t: np.arctan(t * a)  # лямбда выражение (функция)
x2 = lambda t: np.sin(a * t + b)
x3 = lambda t: np.arcsin(a * t + b)
x4 = lambda t: np.cos(a * t + b)
x5 = lambda t: np.arccos(a * t + b)

fig, ax = plt.subplots()
ax.plot(v, x1(v), color="blue", label="arctan(t*a)")
ax.plot(v, x2(v), color="red", label="sin(a*t + b)")
ax.plot(v, x3(v), color="yellow", label="arcsin(a*t + b)")
ax.plot(v, x4(v), color="black", label="cos(a*t + b)")
ax.plot(v, x5(v), color="silver", label="arccos(a*t + b)")
ax.set_xlabel("x")  # подпись у горизонтальной оси х
ax.set_ylabel("y")  # подпись у вертикальной оси y
ax.legend()  # показывать условные обозначения
ax.grid()
plt.show()


