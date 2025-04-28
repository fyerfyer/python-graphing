import numpy as np
import matplotlib.pyplot as plt

# 定义参数
E = 10  # 振幅
f = 10e3  # 频率 (Hz)
T = 1 / f  # 周期 (s)
N = 10  # 计算前 N 项谐波

# 计算频率和幅度谱
n_values = np.arange(-N, N + 1)  # 谐波次数
c_n = E / T  # 所有谐波的幅度相同

# 绘制频谱图
plt.figure(figsize=(8, 5))
plt.stem(n_values * f, np.abs(c_n) * np.ones_like(n_values), basefmt=" ")
plt.title("Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude |c_n|")
plt.grid()
plt.tight_layout()
plt.savefig("frequency_spectrum.png")
plt.show()