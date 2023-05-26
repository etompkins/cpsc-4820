"""
Created on Sun Mar 27 20:02:36 2022

@author: arazi, danny saad
"""

import numpy as np
import matplotlib.pyplot as plt

print('rejection sampling')


#desired probability
def f(x):
    if (np.isscalar(x)):
        x = np.array([x])
    a = np.sqrt(2/(3+np.pi))
    y=x*0    
    for i in range(x.shape[0]):
        if x[i] <= 0 and x[i] > -1*a:
            y[i] = x[i] + a
        elif x[i] >= 0 and x[i] < a:
            y[i] = a
        elif x[i] >= 2*a and x[i] <= 4*a:
            y[i] = np.sqrt(a**2 - (x[i]-3*a)**2)
        else:
            y[i]=0
    return y
            
#baseline probability
def g(x,scale):
    return (scale/np.sqrt(2*np.pi))*np.exp(-x**2/2)
   
    
mode= int(input('Enter 1 for Rejection Sampling, 2 for MCMC Metropolis-Hasting: '))

t = np.arange(-3,+3,0.01)
f1=f(t)
plt.figure()
plt.plot(t,f1,'b')
plt.xlim(-2,3)
plt.show()


# Rejection sampling
if mode==1:
    N=100000
    N_rejected = 0
    scale=20  # make sure scale*f(x)>g(x)
    
    x = np.random.randn(N)
    u = np.random.rand(N)
    xx=[]
    for i in range(N):
        if u[i]<= f(x[i])/g(x[i],scale):  #accept sample
            xx.append(x[i])
        else:
            N_rejected += 1
        
        
        
    print('rejection sampling')
    print(f'rejected = {N_rejected} / {N}')
    g1=g(t,scale)
    plt.plot(t,g1,'r')
    plt.plot(t,f1,'b')
    plt.show()

    plt.figure()
    plt.hist(xx,100, density=True)
    plt.plot(t,f1,'r')
    plt.xlim(-3,3)
    plt.title(f'Histogram of RV generated by Rejection Sampling1 C={scale}') 
    plt.show()

# MCMC Sampling
if mode==2:

    print('MCMC Metropolis-Hasting')

    N=100000
    rejected = 0
    nBins=20
    u = np.random.rand(N)
    r = np.random.randn(N)

    xx=[0] * N
    #xx[0]=0
    for i in range(N-1):
        xnew = xx[i]+r[i] #mew sample from g(y|x)=N(xx,1) 
        alpha=f(xnew)/f(xx[i])
        if u[i] <= alpha:
            xx[i+1]= xnew   #accept
        else:
            xx[i+1]= xx[i]  #reject
            rejected += 1
            
    t = np.arange(-3,+3,0.01)
    f1=f(t)
    plt.figure()
    plt.hist(xx,bins=nBins, density=True)
    plt.xlim(-3,3)
    plt.title('Histogram of RV generated by MCMC Sampling')
    plt.plot(t,f1,'r')
    plt.show()
    print(f'rejected = {rejected} / {N}')
    
    
    
    
    
