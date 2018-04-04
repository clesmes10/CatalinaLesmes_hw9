import numpy as np
import matplotlib.pyplot as plt

datopy = np.genfromtxt("times_python.csv")
datoc = np.genfromtxt("times_cpp.csv")

plt.plot(datopy[:,1], datopy[:,0], "m")
plt.plot(datoc[:,1], datoc[:,0], "c")
plt.xlabel("Tiempo")
plt.ylabel("N")
plt.legend("Tiempo vs N")
plt.savefig("cpp_vs_python.png")
