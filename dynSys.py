#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
THIS FILE: Object definitions linking things together - ONLY FILE MEANT TO BE DIRECTLY INTERFACED WITH

DB DIAGRAM - https://www.lucidchart.com/documents/edit/9275d4dc-d1fb-4327-88f0-46c68caceecd/0

https://pydstool.github.io/PyDSTool/FrontPage.html - similar, take ideas from 
    http://csc.ucdavis.edu/~chaos/courses/nlp/Projects2008/Engle_Whalen/englewhalen_report.pdf also 
    https://github.com/artemyk/dynpy
    https://github.com/simupy/simupy too - block diagrams
        matlab - https://www.mathworks.com/help/simulink/simulink.html
integratable w XPP too? http://www.math.pitt.edu/%7Ebard/bardware/tut/newstyle.html
    should be able to just put in raw EQ file http://www.math.pitt.edu/%7Ebard/bardware/tut/start.html#toc

@TODOs
    Initial Conditions count as special params
    Serializable - intention for DB
        all computed runs should be reduceable to & re-obtainable from System obj (Components aggregated via Equations) & Parameter Values
    Able to run data as stream? 
        options of loop/stop/steptime
        Param sliders update result of fn in real(ish) time
    inputtable as template string
        QT frontend for inputting block diagram - NodeFlow
    can output a NF flowchart of components
    fortran computational backend? - https://arogozhnikov.github.io/2015/11/29/using-fortran-from-python.html
    upload to pypi - https://packaging.python.org/tutorials/packaging-projects/
    Latex formatting
    read object values from json file
    Optional Accounting for Units?
    On Iterate: - PARALLELIZE
        >Transmit from all sources (stateful Systems,Params (& Constants?)) 
        >>Process functions 
            --compact as much as possible
                if single endpoint then just flatten 
                else treat as memoryless node
        >>>all Systems Receive, calculate new State.
        >>>>Events read Transmissions? or before Systems?
"""
import numpy as np

from dynComp import *
from dynViz import *
import DPIO as IO


class Simulation(object):#Master Object - everything User controls goes here, everything packaged up ready to use - connects Ensemble to Integrator, outputs a bunch of States
    pass
class Ensemble(object):#An ensemble is a list of one or more Systems (each of which potentially have different Parameters set) a Topology Adj Mat (default I) 
    def __init__(self,systemList,topMat=np.array((1)),defaultConnStrength=1,*args,**kw):
        pass
class System(object):#Sysetms are a collection of Components fit into a specific connectivity. Coupling Input & Output can be defined for this System ()
    def __init__(self,eqDict,*args,**kw):
        pass
    def defineCoupling(self,coupleDir):#coupling: dict of Component -> Parameter/Slot (how it fits into Equation)
        pass
    def changeParameters(self):#meant to be used for an Ensemble with non-homogenous Parameters 
        pass
#########################

class Equation(object):#how parameters & Variables connect within a system - Differential EQ child of EQ? 
    def __init__(self,template):
        pass
    def Diff(self,wrt,order=1):#wrt is dependant variable, order is how many times to differentiate
        pass
    
#component & function subclasses of Equation?
class Component(Equation):#stateful component of dynamic System  - Differential Equation: composed of set w Variable & definition of its derivative(s) 
    def __init__(self,var,dvars,memorySize=1,*args,**kw):#memorysize -how many steps back each step of the component has access to (-1 -> All steps)   
        pass
class Function(Equation):#EQ with No state, gets computed & immediately sent along 
    def __init__(self,fn,*args,**kw):
        self.fn=fn
#########################

class Slot(object):#generic name for object connected to an "outside" - can be coupled with, can be manipulated
    def __init__(self,name,template,*args,**kw):
        self.name=name
        pass
    #Param,Constant,Variable subclasses of Slots
class Parameter(Slot): 
    def __init__(self,inputrange,defaultvalue,*args,**kw):
        pass
class Constant(Slot):
    def __init__(self,value,*args,**kw):
        self.value=value
class Variable(Slot):#account for derivatives somehow
    def __init__(self,ICs=None,BCs=None,*args,**kw):
        pass
    def updateValue(self):
        pass
#########################
        
class Integrator(object):
    def __init__(self,stepMethod,function,initialDomain,finalDomain,initialRange,numSteps=None,maxStepSize=None,*args,**kw):
        
        if numSteps is not None:
            maxStepSize=(finalDomain-initialDomain)/numSteps
        elif maxStepSize is not None:
            numSteps=round((finalDomain-initialDomain)/maxStepSize)
        else:#both are None
            return None
        
        rangeArray=np.zeros(numSteps+1)
        rangeArray[0]=initialRange
        
        self.maxStepSize=maxStepSize
        self.rangeArray=rangeArray
        self.function=function
        self.initialDomain=initialDomain
        if stepMethod in STEPMETHODS:
            self.stepMethod=stepMethod
        else:
            return None
        
    def runIntegration(self):
        thisDomain=self.initialDomain
        for n in range(len(self.rangeArray)-1):
           thisDomain,self.rangeArray[n+1]=self.stepMethod(function=self.function,thisDomain=thisDomain,thisRange=self.rangeArray[n],maxStepSize=self.maxStepSize)
        return self.rangeArray
#class EulerIntegrator(Integrator):
#    pass
#class RKIntegrator(Integrator):#RK4
#    pass
#########################

class Event(object):#basic logic - emits when logic returns true, called whenever attribute attached to runs 
    def __init__(self,conditional,slot):
        pass
class Manipulation(object):#Subclass of Event? gets input into some saved event list on user action - when in-stream stops calculation
    pass
#########################

class State(object):#would this be useful? saved db result?
    pass  
#########################

class Phaseplot(object):#Phase instead of Phaseplot?
    pass
class Plothandle(object):#object user interacts with which instantiates a Manipulation on System
    pass
#########################

class X(object):
    def __init__(self,*args,**kw):
        pass
class Y(X):
    def __init__(self,*args,**kw):
        pass
#########################