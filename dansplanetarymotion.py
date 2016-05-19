#Dan Walsh, PHY 521, HW4

import numpy as np
import math as ma
import dansode
import visual as vp
import random as rd

GM = 4*vp.pi*vp.pi      # G*Msun
delt = rd.random()

def earth(y, t):# return the eqns of motion
    
    dydt = np.zeros(4)
    dydt[0] = y[2]      # velocity, dr/dt
    dydt[1] = y[3] 
    r = vp.sqrt(y[0]*y[0] + y[1]*y[1]) # acceleration, dv/dt
    dydt[2] = -GM*y[0]/(r*r*r)  
    dydt[3] = -GM*y[1]/(r*r*r)
    return dydt

def go():
    y = [1.0, 0.0, 0.0, ma.pi*1.8] # initial x,y and vx,vy
    
    # draw the scene, planet earth/path, sun/sunlight
    scene = vp.display(title='Planetary motion',
                       background=(.2,.5,1), forward=(0,2,-1))
    planet= vp.sphere(pos=(y[0],y[1]), radius=0.1, 
                      material=vp.materials.earth,up=(0,0,1))
    path  = vp.points(pos=(y[0],y[1]), size=2)
    sun   = vp.sphere(pos=(0,0),radius=0.2,color=vp.color.yellow,
                      material=vp.materials.emissive)
    sunlight = vp.local_light(pos=(0,0), color=vp.color.yellow)
    
    t, h = 0.0, 0.002
    while True:
        vp.rate(200)   # limit animation speed
        y = dansode.RK4n(earth, 4, y, t, h)    # integrate
        t = t + h
        
        planet.pos=(y[0],y[1])                 # move planet
        path.append(pos=(y[0],y[1]))           # draw path
go()
        
