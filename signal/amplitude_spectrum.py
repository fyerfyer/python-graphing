import numpy as np
import matplotlib.pyplot as plt

# 定义参数
E = 10  # 振幅
f = 10e3  # 频率 (Hz)
T = 1 / f  # 周期 (s)
N = 10  # 计算前 N 项傅里叶系数

# 定义傅里叶系数 a_n
def a_n(n):
    if n == 0:
        return E / 2  # 直流分量
    else:
        return (2 * E / (np.pi * n)) * np.sin(n * np.pi / 2)

# 计算傅里叶系数
n_values = np.arange(0, N + 1)
a_values = np.array([a_n(n) for n in n_values])

# 绘制幅度谱
plt.figure(figsize=(8, 5))
plt.stem(n_values, np.abs(a_values), basefmt=" ")
plt.title("Amplitude Spectrum")
plt.xlabel("Harmonic Number (n)")
plt.ylabel("Amplitude |a_n|")
plt.grid()
plt.tight_layout()
plt.savefig("amplitude_spectrum.png")
plt.show()