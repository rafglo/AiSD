import time, matplotlib.pyplot as plt, random, numpy as np
s = list(range(10**7))
times = []
for i in range(1,10**7,10**6):
  t=0
  for k in range(100):
    start = time.time()
    s.pop(i-1)
    end = time.time()
    t+=(end-start)
    s.append(1)
  times.append(t/100)
plt.scatter(range(1,10**7,10**6), times)
plt.show()