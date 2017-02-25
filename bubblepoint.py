# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 20:04:19 2017

@author: James
"""

def sigma_y(y,x):
    sigma=0
    for i in range(1,len(x)):
        sigma=sigma+y[i]
    return sigma
def input_k(k,x):
    for i in range(1,len(x)):
        k[i]=input('enter the new k value of component '+str(i)+': ')
        k[i]=float(k[i])
    return k
def calculate_y(k,x,y):
    for i in range(1,len(x)):
       y[i]=x[i]*k[i]
    return y
def input_initial_k(k,x):
    for i in range(1,len(x)):
        kin=input('the initial value of component '+str(i)+' is: ')
        kin=float(kin)
        k.append(kin)
    return k
def cal_initial_y(k,x,y):
    for i in range(1,len(x)):
        yin=k[i]*x[i]
        y.append(yin)
    return y
        
        
    
def bubblepoint(x,p,guessT):
   
    print('set pressure at '+str(p))
    print('use the guess T to get initial value of k')
    k=[0]
    y=[0]
    input_initial_k(k,x)
    cal_initial_y(k,x,y)
    print('initial k: ',k)
    print('y: ',y)
    sigma=sigma_y(y,x)
    print('sigma: ',sigma)
    while abs(sigma-1)>0.01:
        knew=k[y.index(max(y))]/sigma
        print('the new k of component '+str(y.index(max(y)))+' is '+str(knew))
        input_k(k,x)
        print('k: ',k)
        calculate_y(k,x,y)
        print('y: ',y)
        sigma=sigma_y(y,x)
        print('sigma: ',sigma)