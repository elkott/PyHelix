# -*- coding: utf-8 -*-
"""

HELIXLIB - A SET OF FUNCTIONS TO CONSTRUCT AND MANIPULATE HELICAL OBJECTS

"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv

def getUnitVector(vi, vj, vk):
    v = np.array([vi, vj, vk])
    mag = np.linalg.norm(v)
    unitVector = v/mag
    return unitVector
    

def calculateHelixPoints(R, startDepth, thetaStart, thetaEnd, numOfPoints, parameterB, isOuterProfile):
    x = np.array([])
    y = np.array([])
    z = np.array([])
    ni = np.array([])
    nj = np.array([])
    nk = np.array([])
    inc = (thetaEnd-thetaStart)/(numOfPoints-1)
    for i in range(numOfPoints):
        theta = thetaStart + inc * i
        x = np.append(x, R * np.cos(theta))
        y = np.append(y, R * np.sin(theta))
        z = np.append(z, parameterB * theta)  
        if isOuterProfile:
            normalUnitVector = getUnitVector(R*(R**2+parameterB**2)*np.cos(theta), R*(R**2+parameterB**2)*np.sin(theta), 0)
            ni = np.append(ni, normalUnitVector[0])
            nj = np.append(nj, normalUnitVector[1])
            nk = np.append(nk, normalUnitVector[2])
        else:
            normalUnitVector = getUnitVector(-R*(R**2+parameterB**2)*np.cos(theta), -R*(R**2+parameterB**2)*np.sin(theta), 0)
            ni = np.append(ni, normalUnitVector[0])
            nj = np.append(nj, normalUnitVector[1])
            nk = np.append(nk, normalUnitVector[2])
    
    if z[0] < 0:
        z = z + np.abs(z[0]) + startDepth
    else:
        z = z - z[0] + startDepth
    return [x, y, z, ni, nj, nk]


def storeHelixData(helixDataFilePath, helix):
    with open(helixDataFilePath, 'w', newline='') as csvfile:
     helixwriter = csv.writer(csvfile, delimiter=',',
                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
     helixwriter.writerow(['x'] + ['y'] + ['z'] + ['Ni'] + ['Nj'] + ['Nk'])
     x = helix[0]
     y = helix[1]
     z = helix[2]
     ni = helix[3]
     nj = helix[4]
     nk = helix[5]    
     for i in range(len(x)):
         helixwriter.writerow([x[i] , y[i] , z[i], ni[i], nj[i], nk[i]])


def plotHelix(helix):
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')
    x = helix[0]
    y = helix[1]
    z = helix[2]
    ax1.plot( x, y, z, c='b', label='Helix')
    plt.legend(loc='upper left');
    plt.axis('equal')
    plt.show()

  
def degreeToRadians(thetaDeg):
    return thetaDeg * np.pi/180.0
  

def buildHelix(R, startDepth, thetaStart, numberOfRevolutions, numOfPointsPerRev, pitch, isOuterProfile, helixFileFullName):
    numOfPoints = int(numberOfRevolutions * numOfPointsPerRev)    
    thetaStart = degreeToRadians(thetaStart)
    thetaEnd = degreeToRadians(numberOfRevolutions * 360)
    parameterB = pitch/(2*np.pi)    
    helix = calculateHelixPoints(R, startDepth, thetaStart, thetaEnd, numOfPoints, parameterB, isOuterProfile)
    storeHelixData(helixFileFullName, helix)
    plotHelix(helix)    