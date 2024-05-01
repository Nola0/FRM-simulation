# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:22:36 2024

@author: User
"""

'''
sources of reference
https://math.stackexchange.com/questions/446093/generate-correlated-normal-random-variables 
https://github.com/guillaumeguy/notebooks/blob/main/Correlated_notebooks.ipynb
'''

import numpy as np
import matplotlib.pyplot as plt

def get_cholesky(pair, convergeCorr):
    dim = pair*2
    corr =  np.zeros((dim,dim))
    np.fill_diagonal(corr, 1)
    
    diagOffsetFill = lambda off: np.diag(np.array([convergeCorr,0]*(pair-1)+[convergeCorr]),off)
    corr = np.add(np.add(corr, diagOffsetFill(1)), diagOffsetFill(-1))
    return np.linalg.cholesky(corr)

def LongShortIdentify(p,t,priceDiff,enT,exT):
    if abs(priceDiff[p][t]) > enT and priceDiff[p][t] > 0:
        return (True, 'l1s2')
    if abs(priceDiff[p][t]) > enT and priceDiff[p][t] < 0:
        return (True, 'l2s1')
    if abs(priceDiff[p][t]) < exT:
        return (False,)

def fundSimulate(pair,T,equity,leverage=50):
    
    startPrice = equity*leverage/(pair*2)
    
    # simulate random normal returns for n pairs of underlying assets across T days 
    normVars = np.random.normal(0,0.03,[pair*2,T]) 

    # simulated prices
    convergencePairs = np.dot(get_cholesky(pair,0.999), normVars)
    simPrices = np.array([(np.cumprod(convergencePairs[r]+1)).tolist() for r in range(pair*2)])*startPrice

    # record live Convergence Trades under each pair
    livePositions = {p:(False,) for p in range(pair)}

    # get pair x T numpy array storing simulated price differences within each pair
    priceDiff = np.array([(simPrices[p*2] - simPrices[p*2+1]).tolist() for p in range(pair)])

    # record daily equity in total
    equityDaily = [equity]
    
    # define entering & exiting conditions
    enT, exT = 0.01*startPrice,0.001*startPrice

    for t in range(T):
        for p in range(pair):
            
            if livePositions[p][0] and livePositions[p][1] == 'l1s2':
                equity += priceDiff[p][t-1] - priceDiff[p][t] # floating gain/loss recorded for long s1 & short s2
            if livePositions[p][0] and livePositions[p][1] == 'l2s1':
                equity += priceDiff[p][t] - priceDiff[p][t-1] # floating gain/loss recorded for long s2 & short s1
            
            # if there is a change to trade status, update livePositions
            if LongShortIdentify(p,t,priceDiff,enT,exT) != None:      
                livePositions[p] = LongShortIdentify(p,t,priceDiff,enT,exT) 

        equityDaily.append(equity)

    return np.array(equityDaily)

def simDiagnostic(_iter,pair,T,equity):
    plt.figure(figsize=(20,8),dpi=100)
    for _ in range(_iter):
        plt.plot(np.arange(T+1), fundSimulate(pair,T,equity))
    plt.show()
    
simDiagnostic(_iter=100,pair=10,T=100,equity=100)