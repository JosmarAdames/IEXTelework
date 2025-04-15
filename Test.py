import random
import matplotlib.pyplot as plt
x=[]
for _ in range(10):
    x.append(random.randint(0,11))
    
print(x)

plt.plot(x)
plt.show()