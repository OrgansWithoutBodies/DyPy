#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 00:27:01 2018

@TODOs:
    Parallelize
    RK
    qq  
"""


def euler(function,initialDomain,finalDomain,initialRange,numSteps=None,maxStepSize=None):#returns finalRange estimate by stepping through - uses 2/3 of finalDomain,numSteps,maxStepSize to figure out the other third
#    
#    if finalDomain is not None:#either numsteps xor maxstepsize should be defined
#        []
    if numSteps is not None:
        maxStepSize=(finalDomain-initialDomain)/numSteps
    elif maxStepSize is not None:
        numSteps=round((finalDomain-initialDomain)/maxStepSize)
    else:#both are None
        return None
    rangeArray=np.zeros(numSteps+1)
    
    rangeArray[0]=initialRange
    thisDomain=initialDomain
    for s in range(numSteps):
        rangeArray[s+1]=rangeArray[s]+maxStepSize*function(thisDomain,rangeArray[s])
        thisDomain=thisDomain+maxStepSize
    return rangeArray
def eulerstep():
    pass
    


def rk(): #RK4
    pass

def rkstep():
    pass

