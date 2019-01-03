#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@TODOs:
    Parallelize
    Fix RK scaling
    different RK depths
    integrators can do little bits at a time (saved in state instead & offered break location as specific ICs?)
    
"""
import numpy as np
####
def eulerstep(function,thisDomain,thisRange,maxStepSize):
    
     nextRange=thisRange+maxStepSize*function(domain=thisDomain,range=thisRange)
     nextDomain=thisDomain+maxStepSize
    
     return nextDomain,nextRange


def rkstep(function,thisDomain,thisRange,maxStepSize,RKdepth=4):
    k1=maxStepSize*function(domain=thisDomain,range=thisRange)
    k2=maxStepSize*function(domain=thisDomain+maxStepSize/2,range=thisRange+k1/2)
    k3=maxStepSize*function(domain=thisDomain+maxStepSize/2,range=thisRange+k2/2)
    k4=maxStepSize*function(domain=thisDomain+maxStepSize,range=thisRange+k3)
    
    nextRange=thisRange+1/6*(k1+2*k2+2*k3+k4) 
    nextDomain=thisDomain+maxStepSize
    
    return nextDomain,nextRange


STEPMETHODS={eulerstep,rkstep}