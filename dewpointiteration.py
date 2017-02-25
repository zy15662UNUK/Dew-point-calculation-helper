# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 12:23:34 2017

@author: James
"""
def sigma_x(y,x):
    sigma=0
    for i in range(1,len(y)):
        sigma=sigma+x[i]
    return sigma
def input_k(k,y):
    for i in range(1,len(y)):
        k[i]=input('enter the new k value of component '+str(i)+': ')
        k[i]=float(k[i])
    return k
def calculate_x(k,x,y):
    for i in range(1,len(y)):
       x[i]=y[i]/k[i]
    return x
def input_initial_k(k,y):
    for i in range(1,len(y)):
        kin=input('the initial value of component '+str(i)+' is: ')
        kin=float(kin)
        k.append(kin)
    return k
def cal_initial_x(k,x,y):
    for i in range(1,len(y)):
        xin=y[i]/k[i]
        x.append(xin)
    return x
def dewpointiteration(y,p,guessT):
    print('set pressure at '+str(p))
    print('use the guess T to get initial value of k')
    k=[0]
    x=[0]
    input_initial_k(k,y)
    cal_initial_x(k,x,y)
    print('initial k: ',k)
    print('x: ',x)
    sigma=sigma_x(y,x)
    print('sigma: ',sigma)
    while abs(sigma-1)>0.01:
        knew=k[x.index(max(x))]*sigma
        print('the new k of component '+str(x.index(max(x)))+' is '+str(knew))
        input_k(k,y)
        print('k: ',k)
        calculate_x(k,x,y)
        print('x: ',x)
        sigma=sigma_x(y,x)
        print('sigma: ',sigma)