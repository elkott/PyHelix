# -*- coding: utf-8 -*-
"""
PROGRAM TO CONSTRUCT A HELIX MODEL AND STORE ITS POINTS IN A CSV FILE
"""


import helixLib as hLib



#   SET HELIX CONSTRUCTION PARAMETERS
R = 20
startDepth = 100
startAngle = 0
numberOfRevolutions = 2.25
pitch = 0.1
isOuterProfile = False

#   SET HELIX DATA STORAGE PARAMETERS
numOfPointsPerRev = 50
helixFileFullName = 'helix.dat'


#   CONSTRUCT HELIX AND SAVE EXTRACTED POINTS AND NORMAL VECTORS TO DATA FILE
hLib.buildHelix(R, startDepth, startAngle, numberOfRevolutions, numOfPointsPerRev, pitch, isOuterProfile, helixFileFullName)