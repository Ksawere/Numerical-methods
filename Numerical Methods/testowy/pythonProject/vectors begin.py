import numpy as np
import matplotlib.pyplot as plt
y=0
a1=-2
v1 = np.array(y)
v2 = np.array(a1)
plt.plot(v2, v1, color='blue',linewidth=2,marker='o', markersize=6)
print(a1)
for i in range (v1,6):
    q=-4
    v2 = v2 * q
    print(v2)

    v1+=1
    plt.plot(v2, v1, color='blue',linewidth=2,marker='o', markersize=6)



plt.grid()
plt.title("sequence ")
plt.show()