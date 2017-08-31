# PyHelix
A Python program to generate and store data from a helix equation.

# How to use PyHelix

## Prerequisites
In order to run PyHelix, please place both __helixLib.py__, and __helixGeometry.py__ in the same directory on your local machine.
PyHelix has the following dependencies:
  - _Python:_ This tool was developed using Python3.5
  - _numpy:_ Used to perform numerical operations
  - _matplotlib.pyplot:_ Used to plot the resulting helix
  - _mpltoolkits.mplot3d:_ Used to render 3D axes on Matplotlib
  - _csv:_ Used to store helix points, and normal vectors in a CSV file

If you do not wish to plot the resulting helix, you may omit the code to import, and call _matplotlib.pyplot_, and _mpl_toolkits.mplot3d_ from __helixLib.py__

## Usage
  - Download __helixLib.py__, and __helixGeometry.py__, and place them in the same directory. __helixGeometry.py__ is the main file, and it references the functions defined in __helixLib.py__.
    - Open __helixGeometry.py__, and modify the helix construction parameters:
      - Radius
      - startDepth
      - startAngle
      - numberOfRevolutions
      - pitch
      - isOuterProfile: If __isOuterProfile = False__, the helix unit normal vectors will point towards the helix axis, and vise-versa.
    - Set helix data storage parameters:
      - numOfPointsPerRev: number of points extracted per helix revolution
      - helixFileFullName: CSV [comma-separated] file path, where the helix points and unit normal vectors are to be stored
    - Run __helixGeometry.py__ from within Python console, or using the "Run" command in your favourite Python IDE [_I used Spyder_]. The outcome of running this file will be:
      - a Helix plot appears
      - The helix data is stored in the path specified by the __helixFileFullName__ variable
  
## Example
  
### Helix construction parameters
    
    R = 20
    startDepth = 100
    startAngle = 0
    numberOfRevolutions = 2.25
    pitch = 0.1
    isOuterProfile = False
  
### Helix data storage parameters
    
    numOfPointsPerRev = 50
    helixFileFullName = 'helix.dat'
    
A sample __helix.dat__ file is available in this repository as an example    
