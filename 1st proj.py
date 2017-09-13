# -*- coding: utf-8 -*-

import cantera as ct
import numpy as np
import matplotlib.pyplot as plt

def IgnitionDelay(T,P,X):
    
    gas = ct.Solution('gri30.xml')
    gas.TPX = T, P, X
    
    combustor = ct.IdealGasReactor(gas)
    combustor.volume = 1.0
    
    sim = ct.ReactorNet([combustor])
    
    H_radicals_prev = 0
    H_radicals_now = 0
    
    while H_radicals_prev <= H_radicals_now:
        t = sim.step()
        H_radicals_prev = H_radicals_now
        H_radicals_now = combustor.thermo['H'].X[0]
    
    return 1e6*t if t<1e-2 else -1
    
    
    
    
P_arr1 = np.linspace(0.2, 1, 5)* ct.one_atm
P_arr2 = np.linspace(2,10,5)* ct.one_atm
P_arr = np.concatenate([P_arr1, P_arr2])
    
#P_arr = np.linspace(0.5,10,7)* ct.one_atm
T_arr = np.linspace(1200,3000,40)
X_arr = np.linspace(15.0,150.0,50)/100

T=1500
p=10*ct.one_atm
time = []                   
for x in X_arr:
    X = 'O2:1.0, H2:' + str(x)    
    ignDelTime = IgnitionDelay(T,P,X)
    time.append(ignDelTime)        
plt.plot((X_arr/0.66), time)
plt.xlabel('phi')
plt.ylabel('ignition time [micro second]')
plt.show            

#i=1
#for x in X_arr:
#    X = 'O2:1.0, H2:' + str(x)
#    for P in P_arr:
#        time = []
#        for T in T_arr:
#            ignDelTime = IgnitionDelay(T,P,X)
#            time.append(ignDelTime)
#        print i
#        i=i+1
#        plt.plot(T_arr, time, label="%.2f atm" % (P/ct.one_atm))
#        
#    plt.legend()
#    fig_size = plt.rcParams["figure.figsize"]
#    plt.xlabel('temperature [Kelvin]')
#    plt.ylabel('ignition time [micro second]')
#    fig_size[0] = 12
#    fig_size[1] = 9
#    plt.rcParams["figure.figsize"] = fig_size
#    plt.savefig('plot' + str(x) + '.png')
#    plt.show()
#    plt.close()

#Temp = []
#
#for P in P_arr:
#    T=1100
#    t = 1
#    while t>0:
#        t = IgnitionDelay(T,P,X)
#        T = T - 1
#    print T
#    Temp.append(T)
#plt.plot(Temp,P_arr)
#plt.show()







