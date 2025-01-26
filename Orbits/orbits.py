from math import sqrt, pow
from matplotlib import pyplot as plt
n = 3 #enter the value of n here

x_arr = [0] #in cm
y_arr = [5] #in cm
#vx = float(input("Enter the value of vx: "))
vx = 5 #in cm/s
vy =  0 #in cm/s
x, y = x_arr[-1], y_arr[-1]
r = sqrt(x**2 + y**2)

print(f"Enter the value of k, critical = {vx**2 / pow(r, n+1)}")
k = float(input())

ax = -k * x * pow(r, n-1)
ay = -k * y * pow(r, n-1)
dt = 0.0001 #in s
N = 1000000
for i in range(N):
    vx += (ax * dt)
    vy += (ay * dt)
    x_arr.append(x + vx * dt + 0.5 * ax * dt * dt)
    y_arr.append(y + vy * dt + 0.5 * ay * dt * dt)
    x = x_arr[-1]
    y = y_arr[-1]
    r = sqrt(x**2 + y**2)
    ax = -k * x * pow(r, n-1)
    ay = -k * y * pow(r, n-1)
plt.plot(x_arr, y_arr, color = 'b', label = f'n = {n}')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
