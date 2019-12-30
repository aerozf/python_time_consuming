# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 10:28:18 2019

@author: user
"""

import time


from numba import jit

'''不使用jit装饰，运行时间特别长，例如calc(15)耗时t=56.08s'''
def calc(n, i=0, cols=0, diags=0, trans=0):
    t = time.time()
    if i == n:
        return 1
    else:
        rt=0
        for i in range(n):
            for j in range(10000):
                for k in range(10000):
                   rt+=1 
    print('运行结果：',rt,'\t没有jit装饰代码运行时间：',time.time() - t)
    
'''使用jit装饰，运行效率大大增加，例如jitcalc(15)耗时t=0.0448s'''
@jit    
def jitcalc(n, i=0, cols=0, diags=0, trans=0):
    t = time.time()
    if i == n:
        return 1
    else:
        rt=0
        for i in range(n):
            for j in range(10000):
                for k in range(10000):
                   rt+=1 
    print('运行结果：',rt,'\tjit装饰后代码运行时间：',time.time() - t)

jitcalc(15)  #t=0.0448s
calc(15)     #t=56.08s

            
