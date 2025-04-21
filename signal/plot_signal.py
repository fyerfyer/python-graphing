import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Agg')

# 定义单位阶跃函数 u(t)
def u(t):
    return np.where(t >= 0, 1, 0)

# 定义参数
T = 2  # 周期 T
t = np.linspace(-1, 3 * T, 1000)  # 时间范围

# 信号 (1)
signal_1 = (u(t) - u(t - T)) * np.sin(4 * np.pi * t / T)

# 信号 (2)
signal_2 = (u(t) - 2 * u(t - T) + u(t - 2 * T)) * np.sin(4 * np.pi * t / T)

# 绘制信号 (1)
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, signal_1, label="Signal (1)")
plt.title("Signal (1): [u(t) - u(t - T)] * sin(4πt / T)")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid()
plt.legend()

# 绘制信号 (2)
plt.subplot(2, 1, 2)
plt.plot(t, signal_2, label="Signal (2)", color="orange")
plt.title("Signal (2): [u(t) - 2u(t - T) + u(t - 2T)] * sin(4πt / T)")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid()
plt.legend()

# 保存图形为文件
plt.tight_layout()
plt.savefig("signal_plot.png")