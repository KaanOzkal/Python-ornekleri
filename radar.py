import numpy as np
import matplotlib.pyplot as plt

# Radar parametreleri
max_range = 1000  # maksimum menzil (metre)
range_resolution = 10  # menzil çözünürlüğü (metre)
max_velocity = 100  # maksimum hız (m/s)

# Hedef parametreleri
target_range = 300  # hedefin menzili (metre)
target_velocity = 20  # hedefin hızı (m/s)

# Zaman ve hız bilgisi
t = np.linspace(0, 10, 1000)  # saniye cinsinden zaman
v = np.linspace(-max_velocity, max_velocity, 1000)  # m/s cinsinden hız

# Hedefin radar sinyali
target_signal = np.sinc(2 * target_range / range_resolution) * np.sinc(2 * target_velocity / max_velocity * t[:, np.newaxis])

# Toplam radar sinyali
radar_signal = np.sum(target_signal, axis=1)

# Sinyali görselleştirme
plt.figure(figsize=(10, 5))
plt.plot(t, radar_signal)
plt.title('Radar Sinyali')
plt.xlabel('Zaman (saniye)')
plt.ylabel('Sinyal Şiddeti')
plt.grid(True)
plt.show()
