#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def floor(vector):
    shape=vector.shape
    vector=vector.reshape(-1)
    for i in range(vector.size):
        vector[i]=np.int(vector[i])
 
    vector.reshape(shape)
    return vector

def i_input(u, i):
    con=C[:, i]
    delay=D[:, i]
    temp=np.zeros(N)+u.shape[1]-1
    temp=floor(temp-delay)
    con[temp<0]=0
    temp[temp<0]=0
    pulse=np.zeros(N)
    for j in range(N):
        pulse[j]=u[j, temp[j]]
 
    iinput=np.dot(con, pulse)
    return iinput

def d_u(u, v):
    base=g(u[:, -1], v[:, -1])
    for i in range(u.shape[0]):
        base[i]+=i_input(u, i)
 
    return base

def g(u, v):
    return tau*(-v+gamma*u-u**3/3)

def d_v(u, v):
    return h(u[:, -1], v[:, -1])

def h(u, v):
    return -(-u-a+b*v)/tau

#setting (example)
a=0.7
b=0.2
c=0
gamma=1
N=5
tau=N

t=0
T=100
dt=0.005

#connectivity matrix (example)
C=np.array([[0,1,0,1,1],
            [1,0,1,1,1],
            [0,1,0,1,1],
            [1,1,1,0,0],
            [1,1,1,0,0]])

#length matrix (example)
D=np.array([[0,4,0,5,5],
            [4,0,4,3,3],
            [0,4,0,5,5],
            [5,3,5,0,0],
            [5,3,5,0,0]])

#initial parameters (example)
u=np.array([2, 4, 1, 5, 3]).reshape(-1, 1)
v=np.array([2, 4, 1, 5, 3]).reshape(-1, 1)

t+=dt
while t<T:
    du=d_u(u, v)
    dv=d_v(u, v)
    temp_u=u[:, -1]+du*dt
    temp_v=v[:, -1]+dv*dt
    u=np.c_[u, temp_u]
    v=np.c_[v, temp_v]
    t+=dt

plt.subplot(1, 2, 1)
for i in range(u.shape[0]):
	plt.plot(np.arange(0, u.shape[1], 1)*dt, u[i, :], label='u'+str(i))
	plt.plot(np.arange(0, v.shape[1], 1)*dt, v[i, :], label='v'+str(i))
	plt.legend()

plt.subplot(1, 2, 2)
for i in range(u.shape[0]):
	plt.plot(u[i, :], v[i, :], label='node'+str(i))
plt.legend()

plt.show()

