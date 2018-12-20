#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EQ ORGANIZATION: https://www.lucidchart.com/documents/edit/c15a7865-f309-4d48-947f-f7b00ac05159/0

https://academic.oup.com/brain/article/137/8/2210/2847958#78872443


https://pydstool.github.io/PyDSTool/FrontPage.html - similar, take ideas from 
    http://csc.ucdavis.edu/~chaos/courses/nlp/Projects2008/Engle_Whalen/englewhalen_report.pdf also 
    https://github.com/simupy/simupy too - block diagrams
        matlab - https://www.mathworks.com/help/simulink/simulink.html
integrate XPP too? http://www.math.pitt.edu/%7Ebard/bardware/tut/newstyle.html
    should be able to just put in raw EQ file http://www.math.pitt.edu/%7Ebard/bardware/tut/start.html#toc
@TODOs
    DS HVs w/ Nullclines
    Serializable - intention for DB
    Able to run as Stream?
    inputtable as template string
        QT frontend for inputting block diagram - NodeFlow
    Flowchart of components
"""
import numpy as np
class System(object):#A System is at least one Node with some metadata
    pass
class Nodes(object):#Nodes are a collection of Components fit into a specific connectivity all associated with an integrator. Coupling Input & Output can be defined for this Node ()
    def __init__(self,eqdict):
        pass
class Component(object):#stateful component of dynamic Node 
    pass

class Parameter(object):
    pass

class Variable(object):
    pass

class Equation(object):
    pass

class Integrator(object):
    pass


def eulerintegrator(function,initialDomain,finalDomain,initialRange,numSteps=None,maxStepSize=None):#returns finalRange estimate by stepping through - uses 2/3 of finalDomain,numSteps,maxStepSize to figure out the other third
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
    
def rkintegrator(): #RK4
    pass

